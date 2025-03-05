run:
	mdbook serve
build:
	mdbook build

fab:
	cd book && git init . && git add . &&git commit -m "更新文档" && git branch -M main && git remote add origin git@github.com:ma-guo/niuhebook.git &&git push --force -u origin main && cd ..