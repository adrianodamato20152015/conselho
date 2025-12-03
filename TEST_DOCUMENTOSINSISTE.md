# Testing Guide for documentosinsiste.html

## Quick Test Instructions

### 1. Open the File
Open `documentosinsiste.html` directly in your web browser.

### 2. Initial View (Normal Mode)
- You should see the main interface
- Document management buttons are **HIDDEN**
- This is expected behavior

### 3. Activate Edit Mode
1. Click the **☰ MENU** button (top left)
2. Click **🔒 Editar**
3. Enter password: `1234` (default)
4. Click **Entrar**

**Expected Result:** 
- "🔓 MODO EDIÇÃO ATIVO" indicator appears (top right)
- Edit mode is now active

### 4. Navigate to Documents
1. Click **☰ MENU** button again
2. Click **📁 Documentos**

**Expected Result:**
- Document management screen opens
- "➕ Nova Pasta" button is **VISIBLE**
- "➕ Novo Documento" button is **VISIBLE**

### 5. Create a Folder
1. Click **➕ Nova Pasta**
2. Modal appears with title "📂 Nova Pasta"
3. Enter folder name: "Legislação"
4. Click **✅ Salvar**

**Expected Result:**
- Alert: "✅ Pasta criada!"
- Folder appears in the list with 📂 icon
- Folder shows ▶ arrow to expand/collapse

### 6. Add Document to Folder
1. Click the **➕ Adicionar** button on the folder
2. Modal "➕ Adicionar Item" appears
3. Click **📄 Novo Documento**
4. Enter document name: "Decreto de Criação"
5. Enter URL: "https://example.com/decreto.pdf"
6. Click **✅ Salvar**

**Expected Result:**
- Alert: "✅ Documento criado!"
- Document appears inside the folder
- Document shows 📄 icon

### 7. Test Document Opening
1. Click on the document name
2. **Expected Result:** Link opens in new browser tab

### 8. Edit Folder
1. Click ✏️ button on the folder
2. Modal opens with current name
3. Change name to "Legislação Federal"
4. Click **✅ Salvar**

**Expected Result:**
- Alert: "✅ Pasta atualizada!"
- Folder name changes in the list

### 9. Edit Document
1. Click ✏️ button on the document
2. Modal opens with current name and link
3. Change name or link
4. Click **✅ Salvar**

**Expected Result:**
- Alert: "✅ Documento atualizado!"
- Document name/link updates

### 10. Create Root Document
1. Click **➕ Novo Documento** (main button)
2. Enter name: "Plano de Gestão"
3. Enter URL: "https://example.com/plano.pdf"
4. Click **✅ Salvar**

**Expected Result:**
- Document appears at root level (not inside folder)

### 11. Expand/Collapse Folder
1. Click on folder header (not buttons)
2. **Expected Result:** Folder expands/collapses showing/hiding children

### 12. Delete Document
1. Click 🗑️ button on a document
2. Confirm deletion
3. **Expected Result:** 
   - Alert: "✅ Item removido!"
   - Document disappears from list

### 13. Delete Folder with Content
1. Click 🗑️ button on folder containing items
2. **Expected Result:** 
   - Warning: "⚠️ Esta pasta contém X item(ns). Deseja realmente remover?"
   - Confirm to delete
   - Folder and all contents removed

### 14. Save to JSON
1. Click **☰ MENU**
2. Click **💾 Salvar JSON**
3. **Expected Result:** 
   - JSON file downloads
   - Contains all document structure

### 15. Load from JSON
1. Click **☰ MENU**
2. Click **📂 Abrir JSON**
3. Select the JSON file saved earlier
4. **Expected Result:**
   - Alert: "✅ JSON carregado com sucesso!"
   - All documents and folders restored

### 16. Exit Edit Mode
1. Click **☰ MENU**
2. Click **💾 Finalizar Edição** (shown as colored background)
3. Choose save option

**Expected Result:**
- Edit mode deactivates
- Document buttons **HIDE** again

## Troubleshooting

### Buttons Don't Appear
**Problem:** "➕ Nova Pasta" and "➕ Novo Documento" buttons don't show
**Solution:** 
1. Ensure you're in EDIT mode (look for "🔓 MODO EDIÇÃO ATIVO")
2. Make sure you're on the Documents screen (☰ MENU → 📁 Documentos)

### Modal Doesn't Open
**Problem:** Clicking buttons doesn't open modal
**Solution:**
1. Check browser console for errors (F12)
2. Ensure JavaScript is enabled
3. Try refreshing the page

### Cannot Save Document
**Problem:** Alert says "URL inválida"
**Solution:** URL must start with `http://` or `https://`

### Folder Won't Expand
**Problem:** Clicking folder doesn't expand it
**Solution:** 
1. Click on the folder header/name area
2. Don't click on the ✏️ or 🗑️ buttons
3. Look for the ▶ arrow on the left

## Features Checklist

Use this checklist to verify all features work:

- [ ] Edit mode can be activated
- [ ] Document buttons appear in edit mode
- [ ] Document buttons hidden in normal mode
- [ ] Can create root folder
- [ ] Can create root document
- [ ] Can create nested folder
- [ ] Can create document in folder
- [ ] Can edit folder name
- [ ] Can edit document name and link
- [ ] Can delete document
- [ ] Can delete folder
- [ ] Folder deletion requires confirmation if has content
- [ ] Folders can expand/collapse
- [ ] Clicking document opens link in new tab
- [ ] Can add item inside folder using ➕ Adicionar button
- [ ] Modal "Choose Item Type" works
- [ ] Save to JSON includes documents
- [ ] Load from JSON restores documents
- [ ] Drag and drop works (if in edit mode)

## Success Criteria

✅ **All features working** if:
1. All items in Features Checklist pass
2. No JavaScript errors in console
3. Modals open and close properly
4. Data persists when saved/loaded
5. Buttons show/hide based on edit mode

## Support

If you encounter issues:
1. Check browser console (F12 → Console tab)
2. Verify you're using a modern browser (Chrome, Firefox, Edge, Safari)
3. Ensure JavaScript is enabled
4. Try clearing cache and reloading

---

**File:** documentosinsiste.html  
**Last Updated:** December 3, 2025  
**Status:** ✅ Complete and Functional
