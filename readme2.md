

 需要下载Lyx和texlive这个巨大无比的软件依赖，理论上可以通过类似包管理器的东西定制化封装，但是没明白代理规则，也是为了省时间，当时直接全部下载了，值得注意的是，这个鬼东西还和标准Latex不太一样，用在线latex无法识别。


 每个章节可以自己写自己的，排版和目录会自动化生成，而且几乎不存在奇奇怪怪的格式错乱问题，运行一下脚本就可以自动化生成pdf，理论上可以用pandoc转成docx，但是不清楚什么原因，一旦用了docx排版必乱，反正知网可以识别到pdf，好像也不算是什么硬伤。理论上通过lyx软件修改chapter.lyx就可以,但是要确保结构完整，一年前研究过，不记得了。


 似乎可以通过修改它的Latex模板达到效果看起来和学校pdf模板一样的效果，我用Lyx修改了标题什么的，但是工作量太大遂放弃，因为它在Latex的基础上还有一个python脚本，关于Lyx的手册少之又少，时间限制没办法弄明白。
 
 * 最终输出产物为output.pdf 
 * 下载完texlive和Lyx在Cli内运行make.bat就能生成pdf，调试时记得开git，出了奇怪的问题很方便回档，也可以对比哪个文件出了意料之外的文件。
 * 希望填补一下学校没有Latex模板的空白。 