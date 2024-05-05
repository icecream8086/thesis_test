#!/usr/bin/env python3

import yaml, os, re, sys
import shutil

yfile = 'thesis.yaml' if len(sys.argv) == 1 else sys.argv[1]
meta = yaml.load(open(yfile), Loader=yaml.FullLoader)

# Windows doesn't have rm -rf command, use shutil.rmtree instead
if os.path.exists('build'):
    shutil.rmtree('build')
os.makedirs('build', exist_ok=True)

# Windows doesn't have cp command, use shutil.copy instead
for file in os.listdir('res'):
    if file.endswith('.lyx') or file == 'thesis.layout':
        shutil.copy(os.path.join('res', file), 'build')

def gen(fname):
    with open("build/%s" % fname) as fp:
        contents = fp.read()
        
    def repl(m):
        key = m.group(1).strip()
        if key in meta:
            return str(meta[key])
        else:
            return "\\textcolor{red}{Undefined (%s)}" % key
        
    contents = re.sub(r'-\{\{-(.*?)-\}\}-', repl, contents)

    with open("build/%s" % fname, "w") as fp:
        fp.write(contents)

for f in ['thesis.layout', 'grad.lyx']:
    gen(f)