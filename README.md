# 发布指南
由于生成后每次 book 中的 .git 目录都会被删除, 因此 build 后需要再次执行如下代码

```sh
cd book
git init .
git add .
git commit -m "更新文档"
git branch -M main
git remote add origin git@github.com:ma-guo/niuhebook.git
git push --force -u origin main
```