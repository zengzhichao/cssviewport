# cssviewport
一个将CSS的px值转换为viewport值的Sublime Text 3自动完成插件
=======
CSSVIEWPORT

----------------------

一个将CSS的px值转换为viewport值的Sublime Text 3自动完成插件

参考了

[cssrem](https://github.com/flashlizi/cssrem)

[postcss-px-to-viewport](https://github.com/evrone/postcss-px-to-viewport)

插件效果如下：

![演示效果图](cssviewport.gif)

安装

- 下载项目

- 进入packages目录：Sublime Text -> Preferences -> Browse Packages...

- 复制下载的cssviewport到Packages目录里面

- 重启Sublime Text

  

配置参数

配置文件Sublime Text -> Preferences -> Package Settings -> cssviewport

- disable  - 是否不使用此插件 设置为0就关闭 1就开启 默认为1
- unitToCovert - 需要转换的单位 默认为"px"
- viewportWidth - 设计稿默认的视口宽度 默认为750
- unitPrecision - 单位转换后保留的精度 默认为5
- viewportUnit - 希望使用的视口单位 默认为"vw"
- available_file_types - 启用此插件的文件类型。默认为：[".css", ".less", ".sass"]。
