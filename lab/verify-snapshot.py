import hashlib, json
from pathlib import Path
manifest=json.loads(Path('source-manifest.json').read_text())
for name, expected in manifest['sha256'].items():
    actual=hashlib.sha256(Path(name).read_bytes()).hexdigest()
    assert actual == expected, (name, actual, expected)
print('Frozen workflow sources verified')
