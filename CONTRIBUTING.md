# Contributing to ZENXHAT

Terima kasih minat Anda untuk berkontribusi pada ZENXHAT! Kami menerima kontribusi dari komunitas.

## Code of Conduct

- Gunakan toolkit **hanya untuk tujuan etis dan legal**
- Hormati privasi dan keamanan orang lain
- Tidak ada harassment atau perilaku tidak pantas

## Cara Berkontribusi

### 1. Fork Repository
```bash
git clone https://github.com/YOUR_USERNAME/ZENXHAT.git
git checkout -b feature/new-module
```

### 2. Setup Development Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Create Your Feature
- Buat module baru di `zenxhat/modules/`
- Ikuti naming convention: `snake_case.py`
- Tambahkan docstrings dan comments
- Gunakan logging untuk debugging

### 4. Testing
```bash
python -m pytest
flake8 zenxhat/
black zenxhat/
```

### 5. Push dan Create Pull Request
```bash
git add .
git commit -m "Add new feature: description"
git push origin feature/new-module
```

## Guidelines

✅ **DO:**
- Write clean, readable code
- Add proper documentation
- Include error handling
- Use passive reconnaissance only
- Test thoroughly

❌ **DON'T:**
- Active scanning/port scanning tanpa izin
- Exploit code atau vulnerability details
- Bypass authentication
- Collect private data
- Remove ethics/legal warnings

## Reporting Issues

Kalau menemukan bug:
1. Check existing issues dulu
2. Buat issue baru dengan:
   - Clear title
   - Detailed description
   - Steps to reproduce
   - Expected vs actual behavior

## Module Structure

```python
"""Module description"""

import necessary_libraries
from zenxhat.core.logger import setup_logger
from zenxhat.core.utils import validation_functions

logger = setup_logger(__name__)

class ModuleName:
    """Class documentation"""
    
    def __init__(self):
        self.logger = logger
    
    def public_method(self):
        """Method documentation with return type"""
        try:
            # Implementation
            self.logger.info("Action taken")
            return result
        except Exception as e:
            self.logger.error(f"Error occurred: {str(e)}")
            return None
```

## Questions?

Contact: zenCTRLalt@protonmail.com

---

Thank you for contributing! 🚀
