一个 Alfred Workflow，可以上传剪切板图片到新浪微博，并复制 URL 到剪切板
详情和制作过程见：

[](https://imciel.com/2016/07/17/weibo-picture-upload-alfred-workflow/)

### 使用
在 [Release](https://github.com/cielpy/WeiboPictureWorkflow/releases) 页下载最新的 Workflow 安装即可，安装完成后设置自己的快捷键

![](https://ww3.sinaimg.cn/large/74681984gw1f5xbkf7f9oj20nh0geabb)

上方是单独生成 URL 的，下方是生成 Markdown 格式字符串的，可以根据自己的喜好设置。

设置快捷键完成后，按快捷键激活 Workflow，会提示没有，并打开一个配置文件，需要在这个文件中输入微博用户名和密码，用于模拟登录，登录完成后会删除这个配置文件。

登录完成后就可以上传图片了，截图或者复制一张图片，按刚才设置的快捷键，上传完成后会有提示。提示 URL 已复制到剪切板的话，说明已经上传成功，这个时候就可以粘贴到你想要粘贴的地方了。


