import os
import shutil
import json
import subprocess
import sys

path = os.path.dirname(os.path.realpath(__file__))
output = os.path.join(path, "output")
config = os.path.join(path, "config.json")
settings_file = os.path.join(path, "settings.tex")
template = os.path.join(path, "template.tex")
out_pdf = os.path.join(path, "out.pdf")

verbose = sys.argv[1:].__contains__("-v")

if not os.path.exists(config):
    print("Config file not found")
    exit(1)

if os.path.exists(output):
    shutil.rmtree(output)


os.mkdir(output)

with open(config) as f:
    json_data = json.load(f)

university_id = json_data['universityID']
pages = json_data['pages']
modules = json_data['modules']

tex_settings = [f"\\userid{{{university_id}}}\n", f"\\pages{{{pages}}}"]

with open(settings_file, "w+") as f:
    f.writelines(tex_settings)

pdflatex_result = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-jobname=out", template],
                                 stderr=subprocess.STDOUT, stdout=subprocess.PIPE)

if pdflatex_result.returncode != 0:
    print("Error: pdflatex exited with a non-zero return code. Run with -v to show the output of pdflatex")
    if verbose:
        print(pdflatex_result.stdout.decode("utf-8"))

for module in modules:
    module_pdf = os.path.join(output, f"{module}_{university_id}.pdf")
    shutil.copyfile(out_pdf, module_pdf)

os.remove("out.aux")
os.remove("out.log")
os.remove("out.pdf")
