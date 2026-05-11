"""
Патчит seminar_notebook.ipynb:
  - Заменяет os.environ["CUDA_VISIBLE_DEVICES"] на авто-определение device (cuda/mps/cpu)
  - Заменяет torch.device("cuda") -> device
  - Заменяет .cuda() -> .to(device)
  - Убирает fused=True из AdamW
"""
import json
import re

NOTEBOOK_PATH = "neuralrec/examples/seminar_notebook.ipynb"

with open(NOTEBOOK_PATH, "r", encoding="utf-8") as f:
    nb = json.load(f)

DEVICE_DETECTION_BLOCK = (
    'import torch\n'
    '\n'
    '# Автоматический выбор устройства (CUDA -> MPS -> CPU)\n'
    'if torch.cuda.is_available():\n'
    '    device = torch.device("cuda")\n'
    'elif torch.backends.mps.is_available():\n'
    '    device = torch.device("mps")\n'
    'else:\n'
    '    device = torch.device("cpu")\n'
    '\n'
    'print(f"Using device: {device}")'
)

def patch_source(source_lines: list[str]) -> list[str]:
    source = "".join(source_lines)

    # Пропускаем DDP ячейку (%%writefile) — она для мультигпу серверов
    if '%%writefile' in source:
        return source_lines

    # Заменяем первую ячейку с CUDA_VISIBLE_DEVICES на блок авто-определения
    if 'CUDA_VISIBLE_DEVICES' in source:
        lines = DEVICE_DETECTION_BLOCK.splitlines(keepends=False)
        return [l + '\n' for l in lines[:-1]] + [lines[-1]]

    # torch.device("cuda") -> device  (в обоих вариантах кавычек)
    source = re.sub(r'torch\.device\(["\']cuda["\']\)', 'device', source)

    # .cuda() -> .to(device)
    source = source.replace('.cuda()', '.to(device)')

    # device="cuda" (в PrefetchDataLoader) -> device=device
    source = re.sub(r'device\s*=\s*["\']cuda["\']', 'device=device', source)
    source = re.sub(r'device\s*=\s*torch\.device\(["\']cuda["\']\)', 'device=device', source)

    # fused=True убираем
    source = re.sub(r',\s*fused\s*=\s*True', '', source)
    source = re.sub(r'fused\s*=\s*True,?\s*', '', source)

    # убираем os.environ CUDA_VISIBLE_DEVICES
    source = re.sub(r'import os\n', '', source)
    source = re.sub(r'os\.environ\[["\']CUDA_VISIBLE_DEVICES["\']\]\s*=\s*.+\n?', '', source)

    lines = source.splitlines(keepends=True)
    return lines

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        cell['source'] = patch_source(cell['source'])

with open(NOTEBOOK_PATH, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=2)

print("✅ Готово! Ноутбук пропатчен. Открой его и запускай.")
