import ast
import importlib.metadata
import sys


standard_libs = set(sys.builtin_module_names)  # Python'un yerleşik modüllerinin isimlerini alır
standard_libs.update({"os", "sys", "math", "time", "datetime", "re", "json", "subprocess", "tkinter"})

def find_imports_and_versions(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())
    imports = [alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names]
    imports += [node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)]

    print("Bulunan importlar:", imports)

    modules_with_versions = {}
    for module in imports:
        if module not in standard_libs:  # Standart kütüphaneler hariç tutuluyor
            try:
                
                version = importlib.metadata.version(module)
                modules_with_versions[module] = version
            except importlib.metadata.PackageNotFoundError:
                modules_with_versions[module] = "unknown"

    return modules_with_versions

def save_requirements(modules, output_file="requirements.txt"): # requirements.txt yolunu ekleyin.
    with open(output_file, "w", encoding="utf-8") as f:
        for module, version in modules.items():
            # Eğer versiyon "unknown" ise, sadece modül ismini yaz
            if version != "unknown":
                f.write(f"{module}=={version}\n")
            else:
                f.write(f"{module}\n")

file_path = "dosya.py"  # Buraya analiz etmek istediğiniz dosyanın adını ve yolu yazın

modul_listesi = find_imports_and_versions(file_path)
if modul_listesi:
    save_requirements(modul_listesi)
    print(f"Kullanılan modüller {file_path} dosyasından alındı ve 'requirements.txt' dosyasına kaydedildi.")
else:
    print("Modül bulunamadı.")
