# Quick Start Guide - segredo_completo.html

## 🚀 Getting Started

### Opening the File
1. Download `segredo_completo.html` to your computer
2. Double-click the file to open it in your default browser
3. Or right-click → Open with → Choose your preferred browser

### First Use
The system starts empty. You have several options:

#### Option 1: Load Example Data
1. Click **☰ MENU** (top left)
2. Click **📥 Carregar Dados Exemplo**
3. System loads with sample council members and data

#### Option 2: Import Your Data
1. Click **☰ MENU** (top left)
2. Click **📂 Abrir JSON**
3. Select your previously exported JSON file

#### Option 3: Start Fresh
1. Click **☰ MENU** (top left)
2. Click **🔒 Editar**
3. Enter the password (default: `admin123`)
4. Start adding members, chambers, etc.

## 🔐 Edit Mode

### Entering Edit Mode
1. **☰ MENU** → **🔒 Editar**
2. Enter password: `admin123` (or your custom password)
3. Screen shows: **🔓 MODO EDIÇÃO ATIVO**

### In Edit Mode You Can:
- ✏️ Edit all text fields (click to edit)
- ➕ Add sectors and positions
- 🗑️ Remove items
- 📂 Create folders and add documents
- 🖱️ Drag & drop to reorder
- 👥 Manage council members
- 🎨 Change background colors

### Exiting Edit Mode
1. **☰ MENU** → **💾 Finalizar Edição**
2. Choose:
   - **✅ SALVAR E FINALIZAR** (recommended)
   - **❌ FINALIZAR SEM SALVAR** (loses changes)
   - **↩️ CONTINUAR EDITANDO** (stay in edit mode)

## 📁 Document Management

### Viewing Documents
1. **☰ MENU** → **📁 Documentos**
2. Click folders to expand/collapse
3. Click documents to open links

### Adding Documents (Edit Mode)
1. Enter edit mode first
2. Go to Documents screen
3. Click **➕ Nova Pasta** or **➕ Novo Documento**
4. Fill in the form:
   - **Folder**: Just needs a name
   - **Document**: Needs name + URL
5. Click **✅ Salvar**

### Organizing Documents
- **Expand folder**: Click on folder name
- **Reorder items**: Drag and drop (edit mode)
- **Edit item**: Click **✏️** button (edit mode)
- **Delete item**: Click **🗑️** button (edit mode)

## 🕵️ Easter Egg - System Reset

### What is it?
A hidden feature to completely reset the system to factory defaults.

### How to Access
1. **Must be in edit mode** (won't work otherwise)
2. Look at the subtitle: "Gestão **Completa** de Membros e Atividades"
3. In edit mode, the word **"Completa"** becomes clickable
4. Click it to open the reset modal

### What Happens?
- Opens warning modal
- Lists everything that will be deleted:
  - All council members
  - All chambers
  - All documents
  - All activities
  - All meeting history
- Requires confirmation
- **Cannot be undone!**

### When to Use
- Starting completely fresh
- After testing with dummy data
- Preparing for a new council term
- Fixing corrupted data

### Safety Tips
- ⚠️ Export your data first (**💾 Salvar JSON**)
- ⚠️ Only use if you're absolutely sure
- ⚠️ Keep backups of important data
- ⚠️ Don't share this feature with unauthorized users

## 💾 Saving Your Work

### Auto-Save
- Changes are saved automatically to your browser's localStorage
- Works offline
- Persists between sessions

### Manual Export
**JSON Export** (recommended for backups):
1. **☰ MENU** → **💾 Salvar JSON**
2. Downloads a `.json` file
3. Keep this file safe as backup

**HTML Export** (complete standalone copy):
1. **☰ MENU** → **🌐 Salvar HTML**
2. Downloads a complete HTML file
3. Includes all your data
4. Can be opened independently

## 🎨 Customization

### Change Background
1. **☰ MENU** → **🎨 Paleta de Cores**
2. Choose from 8 gradient options
3. Click to apply immediately

### Change Password
1. Edit the source code (advanced users)
2. Search for `senhaAdmin`
3. Change the value

## 📋 Meeting Mode

### Start a Meeting
1. **☰ MENU** → **📋 Modo Reunião**
2. Enter date and location
3. Click **✅ Iniciar Lista de Presença**

### Mark Attendance
- Click colored circles next to each member:
  - 🟢 **Green** = Present
  - 🟡 **Yellow** = Justified absence
  - 🔴 **Red** = Absent
- Only shows last 5 meetings per member

### End Meeting
1. Click **✅ CONCLUIR REUNIÃO** (bottom of screen)
2. Or click **❌ ABORTAR REUNIÃO** to cancel

## 📊 Reports and Analysis

### View Reports
1. **☰ MENU** → **📊 Análises**
2. Choose report type:
   - **📋 Composição**: Member list by sector
   - **🗺️ Estados**: Distribution by state
   - **✅ Atividades**: Activities report
   - **📅 Presenças**: Attendance report

### Export Reports
1. Open desired report
2. Click **🖨️ Gerar PDF** (uses browser print)
3. Choose "Save as PDF"

## ⚙️ Advanced Features

### Drag & Drop
**Members to Chambers**:
- Drag member card → Drop on chamber
- Automatically adds member to chamber

**Documents** (edit mode only):
- Drag folders/documents to reorder
- Blue line shows where item will drop
- Works within same level

### Curriculum Management
- Click **📄 Ver Currículo** on any member
- Add biography, qualifications, experience
- Edit in edit mode

### Working Groups (GTs)
- Create within chambers
- Add activities to GTs
- Track progress independently

## 🆘 Troubleshooting

### Changes Not Saving
- Check if you're in edit mode
- Try manual export (JSON)
- Clear browser cache and reload

### Can't Enter Edit Mode
- Password is case-sensitive
- Default: `admin123`
- Clear password field and try again

### Documents Not Opening
- Check URL is complete (http:// or https://)
- Verify link is still valid
- Browser may block popups - allow them

### Lost Data
- Check if you have a JSON backup
- Try: **📂 Abrir JSON** to restore
- If no backup, data cannot be recovered

### Reset Not Working
- Must be in edit mode first
- Word must be clicked directly
- If still not working, reload page

## 📱 Mobile Use

- Fully responsive design
- Touch-friendly buttons
- Swipe to scroll
- May need landscape mode for tables

## 🔒 Security Notes

- All data stored locally in browser
- No external server communication
- Password is stored in the HTML file
- Change default password for security
- Regular backups recommended

## 🌐 Browser Compatibility

✅ **Recommended**:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

⚠️ **May have issues**:
- Internet Explorer (not supported)
- Very old browser versions

## 📚 Additional Resources

- **FEATURES_SEGREDO_COMPLETO.md**: Detailed feature list
- **SUMMARY.md**: Technical implementation details
- **COMPARISON.md**: Comparison with app47.html
- **validate_segredo.py**: Validation script for developers

## 💡 Tips and Tricks

1. **Keyboard shortcuts**: Use Tab to navigate forms
2. **Quick edit**: Double-click text in edit mode
3. **Bulk operations**: Export JSON, edit file, re-import
4. **Testing**: Use "Carregar Dados Exemplo" in a separate browser
5. **Presentation**: Exit edit mode for clean view
6. **Backup routine**: Export JSON weekly
7. **Version control**: Date your JSON exports

## 🎯 Best Practices

1. ✅ Export JSON after major changes
2. ✅ Exit edit mode when not editing
3. ✅ Verify URLs before adding documents
4. ✅ Use clear, descriptive names
5. ✅ Test meeting mode before actual meetings
6. ✅ Keep backups in multiple locations
7. ✅ Don't share edit password publicly
8. ✅ Update attendance regularly

---

**Need Help?**
- Review the documentation files
- Check troubleshooting section
- Ensure you're using a modern browser
- Verify you have necessary permissions

**Enjoy using segredo_completo.html! 🎉**
