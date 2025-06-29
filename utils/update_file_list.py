def update_file_list(files,selected_files,lbl_selected):
        added = 0
        for file in files:
            if file not in selected_files and file.lower().endswith((".jpg", ".jpeg", ".png")):
                selected_files.append(file)
                added += 1
        if added:
            lbl_selected.config(text=f"{len(selected_files)} file(s) selected", foreground="white")
        else:
            lbl_selected.config(text="No new images added", foreground="gray")