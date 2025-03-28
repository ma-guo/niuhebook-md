run:
	mdbook serve

build:
	mdbook build

fab:
	mdbook build
	cd book && git init . && git add . &&git commit -m "更新文档" && git branch -M main && git remote add origin git@gitcode.com:dequankim/niuhebook.git && git push --force -u origin main && cd ..
push:
	mdbook build
	fab -f script/fab.py deployproduct