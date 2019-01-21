hi，小杨, 这是我最近在看的github的一些笔记，可以作为参考了解一下，不多，但能够用了。

1. 创建一个Repository
   我们的项目托管在这里，类似于创建一个QQ空间，这样就有一个自己的库了。在网页里就有Create a New Repository，填好名称后Create，之后会出现一些仓库的配置信息。在我的账号下创建了新的仓库wecare，url是：               https://github.com/JerryMazeyu/wecare.git

2. 配置git
   新建仓库之后，需要和本机进行交互，比我我用shell或者bash命令可以git clone git commit等，这就需要配置一波ssh key，有了这个密钥，github和我们本机之间就有了暗号，可以进行连接了。
   具体呢，首先，在终端输入：
   ssh-keygen -t rsa -C "your_email@youremail.com"
   后面的your_email@youremail.com改为你在github上注册的邮箱，之后会要求确认路径和输入密码，我们这使用默认的一路回车就行。成功的话会在~/下生成.ssh文件夹，进去，打开id_rsa.pub，复制里面的key。
   回到github上，进入Account Settings（账户配置），左边选择SSH Keys，Add SSH Key,title随便填，粘贴在你电脑上生成的key。
   需要注意的是：首先，如果之前已经生成了sshkey的话要覆盖一下；其次，凡是.XXX文件夹的都是隐藏的文件夹，在bash中输入的命令应该是cd ~ / ls -a / cd .sh / cat id_rsa.pub
   相关操作图看这个就好：
   http://www.runoob.com/wp-content/uploads/2014/05/github-account.jpg
   为了验证是否成功，在git bash下输入：
   ssh -T git@github.com
如果是第一次的会提示是否continue，输入yes就会看到：You've successfully authenticated, but GitHub does not provide shell access 。这就表示已成功连上github。

3. 设置用户名和email
   接下来我们要做的就是把本地仓库传到github上去，在此之前还需要设置username和email，因为github每次commit都会记录他们。
   git config --global user.name "your name"
   git config --global user.email "your_email@youremail.com"
   然后在bash中进入你要加入git的文件夹（windows直接最准指定文件夹右键-git bash here）
   git remote add origin git@github.com:yourName/yourRepo.git
   在这里，我输入的是：
   git remote add origin git@github.com:JerryMazeyu/wecare.git（这是因为我之前用了这个用户名创建了这个repo）
   这样的话，你的指定文件夹和远程的库就建立了联系。顺便提一句，linux操作的内核是不报错就是成功，所以刚才这三步不回有任何的提示，如果你想检验一下，可以进入你所指定的文件夹，然后ls -a，这样的话你可以看到里面有一个.git文件夹，进去后有一个config文件，看看是不是都写在里面了。

4. 做到这里，你需要做些什么呢？   
   对于小杨，具体来说，我们的工作是需要在wecare文件夹里面进行，我们要建立我的”本机文件夹wecare-github库wecare-你的本机文件夹wecare之间“的联系，我已经用我的本机的wecare和github上的库联系起来了，你需要做的是先从github上把这个库克隆下来，然后我们一起在这个大文件夹里面分小文件夹，一步一步把项目完成。具体的git clone这种操作，你应该早就试过，不过我还是记录一下，怕忘记。

5. 如何git clone？
   有两种git clone方式，一种是本地之间的copy，其实简单的复制黏贴是一样的。
   命令行是：
   git clone /path/to/repository 比如：git clone ～/mazeyu/wecare/wecare(这是我刚才建立库的地方) ./balala（这是我随便建的一个新文件夹）
   从本地复制库这是为什么呢？这是因为很多个版本之间有时候会很乱，至少备份三个库，相信我，血的经验告诉你，肯定没错的，狡兔三窟稳稳的。
   还有第二种，是从git上面拉库下来，这也是刚才第五点里面你需要做的。（********）脚本为：
   git clone <库名.git> <位置>
   比如： git clone https://github.com/JerryMazeyu/hello-world.git ./balala

6. 用git的具体步骤
   步骤：(确保cd到在你要的文件夹里) 1. git clone 远程库 -- 2. git init 确认一下这个库连接的是这个 -- 3. 在这个库里面修改代码 -- 4. git add <修改过的文件> （git add *）/ (git rm --cached <不需要的文件名>) -- 5. git status (看看状态，哪些是改过的、哪个是新的文件) -- 6. git commit -m 'first commit'（自己写的评论） -- 7. 连接你的库git remote add origin https://github.com/JerryMazeyu/wecare.git(从github上拉下来的库并不需要) -- 8. git pull --rebase origin master(可以把master换成你要的分支) -- 9. git push -u origin master -- 10. 输入用户名和密码 -- 11. git status 看看新状态

7. 关于修改分支
   分支是用来将特性开发绝缘开来的。在你创建仓库的时候，master 是"默认的"分支。在其他分支上进行开发，完成后再将它们合并到主分支上。
   http://www.runoob.com/wp-content/uploads/2014/05/branches.png（示意图）
   创建一个叫做"feature_x"的分支，并切换过去：
   git checkout -b feature_x
   切换回主分支：
   git checkout master
   再把新建的分支删掉：
   git branch -d feature_x
   除非你将分支推送到远端仓库，不然该分支就是不为他人所见的：
   git push origin <branch>
   要合并其他分支到你的当前分支（例如 master），执行：
   git merge <branch>
   在这两种情况下，git 都会尝试去自动合并改动。遗憾的是，这可能并非每次都成功，并可能出现冲突（conflicts）。 这时候就需要你修改这些文件来手动合并这些冲突（conflicts）。改完之后，你需要执行如下命令以将它们标记为合并成功：
   git add <filename>
在合并改动之前，你可以使用如下命令预览差异：
   git diff <source_branch> <target_branch>

8. 替换本地改动
   假如你操作失误（当然，这最好永远不要发生），你可以使用如下命令替换掉本地改动：
   git checkout -- <filename>
   此命令会使用 HEAD 中的最新内容替换掉你的工作目录中的文件。已添加到暂存区的改动以及新文件都不会受到影响。
   假如你想丢弃你在本地的所有改动与提交，可以到服务器上获取最新的版本历史，并将你本地主分支指向它：
   git fetch origin
   git reset --hard origin/master
   
9. 有哪些是需要注意的呢？
  首先，在提交的过程中要注意，每次的提交都只有你修改的文件放进，如果有.gitattribute 这种文件，要拿出来；其次，要多备份几个库，不要没有库，那会很麻烦。












