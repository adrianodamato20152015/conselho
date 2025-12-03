#!/usr/bin/env python3
"""
Validation script for segredo_completo.html
Checks that all required features are present
"""

import re
import sys

def validate_file(filename):
    """Validate the HTML file has all required features"""
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks = []
    
    # 1. Check Easter Egg HTML
    checks.append({
        'name': 'Easter Egg HTML - span#palavraSecreta',
        'pattern': r'<span id="palavraSecreta">Completa</span>',
        'required': True
    })
    
    # 2. Check Easter Egg CSS
    checks.append({
        'name': 'Easter Egg CSS - cursor pointer in edit mode',
        'pattern': r'\.edit-mode #palavraSecreta.*cursor:\s*pointer',
        'required': True
    })
    
    # 3. Check Reset Modal
    checks.append({
        'name': 'Reset Modal HTML',
        'pattern': r'<div class="modal" id="modalResetSistema">',
        'required': True
    })
    
    # 4. Check Reset Functions
    checks.append({
        'name': 'Reset Function - resetarSistemaCompleto',
        'pattern': r'function resetarSistemaCompleto\(\)',
        'required': True
    })
    
    checks.append({
        'name': 'Reset Function - confirmarResetSistema',
        'pattern': r'function confirmarResetSistema\(\)',
        'required': True
    })
    
    # 5. Check Document Container CSS
    checks.append({
        'name': 'Document Container - max-width 1200px',
        'pattern': r'\.documentos-container\s*{[^}]*max-width:\s*1200px',
        'required': True
    })
    
    # 6. Check Document Title CSS
    checks.append({
        'name': 'Document Title - gradient background',
        'pattern': r'\.documentos-titulo\s*{[^}]*background:.*gradient.*#ffeaa7.*#fdcb6e',
        'required': True
    })
    
    # 7. Check Folder Styles
    checks.append({
        'name': 'Folder Header - gradient background',
        'pattern': r'\.pasta-header\s*{[^}]*background:.*gradient.*#fff3e0.*#ffe0b2',
        'required': True
    })
    
    # 8. Check Document Item Styles
    checks.append({
        'name': 'Document Item - gradient background',
        'pattern': r'\.documento-item\s*{[^}]*background:.*gradient.*#e3f2fd.*#bbdefb',
        'required': True
    })
    
    # 9. Check Drag & Drop Functions
    checks.append({
        'name': 'Drag & Drop - configurarDragDropDocumentos',
        'pattern': r'function configurarDragDropDocumentos\(\)',
        'required': True
    })
    
    checks.append({
        'name': 'Drag & Drop - handleDragStartDoc',
        'pattern': r'function handleDragStartDoc\(',
        'required': True
    })
    
    checks.append({
        'name': 'Drag & Drop - handleDropDoc',
        'pattern': r'function handleDropDoc\(',
        'required': True
    })
    
    # 10. Check Easter Egg Event Listener
    checks.append({
        'name': 'Event Listener - palavraSecreta click',
        'pattern': r'palavraSecreta.*addEventListener.*click.*resetarSistemaCompleto',
        'required': True
    })
    
    # 11. Check Edit Mode Buttons
    checks.append({
        'name': 'Edit Mode Buttons CSS',
        'pattern': r'\.edit-mode \.btn-criar-pasta-raiz',
        'required': True
    })
    
    # 12. Check Dragging CSS
    checks.append({
        'name': 'Dragging State CSS',
        'pattern': r'\.pasta-item\.dragging|\.documento-item\.dragging',
        'required': True
    })
    
    # Run all checks
    passed = 0
    failed = 0
    
    print("=" * 70)
    print("VALIDATING segredo_completo.html")
    print("=" * 70)
    print()
    
    for check in checks:
        name = check['name']
        pattern = check['pattern']
        required = check['required']
        
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        
        if match:
            print(f"✅ PASS: {name}")
            passed += 1
        else:
            status = "❌ FAIL" if required else "⚠️  WARN"
            print(f"{status}: {name}")
            if required:
                failed += 1
    
    print()
    print("=" * 70)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 70)
    
    # Additional file stats
    lines = content.count('\n')
    chars = len(content)
    
    print()
    print("FILE STATISTICS:")
    print(f"  Lines: {lines:,}")
    print(f"  Characters: {chars:,}")
    print(f"  Size: {chars/1024:.1f} KB")
    
    return failed == 0

if __name__ == '__main__':
    success = validate_file('segredo_completo.html')
    sys.exit(0 if success else 1)
