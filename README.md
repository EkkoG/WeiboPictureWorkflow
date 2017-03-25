一个 Alfred Workflow，可以上传剪切板图片到新浪微博，并复制 URL 到剪切板
详情和制作过程见：

[https://imciel.com/2016/07/17/weibo-picture-upload-alfred-workflow/](https://imciel.com/2016/07/17/weibo-picture-upload-alfred-workflow/)

### 使用方法

在 [Release](https://github.com/cielpy/WeiboPictureWorkflow/releases) 页下载最新的 Workflow 安装即可，安装完成后设置自己的快捷键

![](https://github.com/cielpy/WeiboPictureWorkflow/blob/master/images/74681984gw1f5xbkf7f9oj20nh0geabb.jpeg)

上方是单独生成 URL 的，下方是生成 Markdown 格式字符串的，可以根据自己的喜好设置。

设置快捷键完成后，按快捷键激活 Workflow，会提示没有，并打开一个配置文件，需要在这个文件中输入微博用户名和密码，用于模拟登录，登录完成后会删除这个配置文件。

登录完成后就可以上传图片了，截图或者复制一张图片，按刚才设置的快捷键，上传完成后会有提示。提示 URL 已复制到剪切板的话，说明已经上传成功，这个时候就可以粘贴到你想要粘贴的地方了。

#### 对于 Alfred 2 用户

由于本人日常使用 Alfred 3，开发也使用的 Alfred 3，导出的 workflow 不能在 Alfred 2 上使用，深感抱歉，这里提供一个办法可以使 Alfred 2 用户也能使用这个 Workflow

1. 安装 [Release](https://github.com/cielpy/WeiboPictureWorkflow/releases) 中最新版本的 Workflow
2. 下载 Alfred 2 专用的 info.plist 文件，链接 https://github.com/cielpy/WeiboPictureWorkflow/blob/master/info_for_v2.plist?raw=true
3. 在 Workflow 列表中找到本 Workflow，右键 Show in Finder，使用第 2 步下载下来的 plist 文件替换掉目录下的 info.plist 文件即可。

### 鸣谢

此项目中很多源码取自 https://github.com/tiann/markdown-img-upload 和 https://github.com/trytofix/hexo_weibo_image ，在这里非常感谢两位作者的付出。


