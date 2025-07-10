# TODO: Translation updated at 2025-07-09 16:06

# game/tutorial_atl.rpy:208
translate zh_cn tutorial_positions_a09a3fd1:

    # e "In this tutorial, I'll teach you how Ren'Py positions things on the screen. But before that, let's learn a little bit about how Python handles numbers."
    e "在本教程中，我将教你Ren'Py如何在屏幕上定位元素。但在此之前，我们先了解下Python处理数字的基本方式。"

# game/tutorial_atl.rpy:210
translate zh_cn tutorial_positions_ba39aabc:

    # e "There are two main kinds of numbers in Python: integers and floating point numbers. An integer consists entirely of digits, while a floating point number has a decimal point."
    e "Python中主要有两种数字类型：整数(integers)和浮点数(floating point numbers)。整数完全由数字组成，而浮点数包含小数点。"

# game/tutorial_atl.rpy:212
translate zh_cn tutorial_positions_a60b775d:

    # e "For example, 100 is an integer, while 0.5 is a floating point number, or float for short. In this system, there are two zeros: 0 is an integer, and 0.0 is a float."
    e "例如，100是整数，而0.5是浮点数(简称float)。在此系统中有两个零：0是整数，0.0是浮点数。"

# game/tutorial_atl.rpy:214
translate zh_cn tutorial_positions_7f1a560c:

    # e "Ren'Py uses integers to represent absolute coordinates, and floats to represent fractions of an area with known size."
    e "Ren'Py使用整数表示绝对坐标，用浮点数表示已知尺寸区域的比例位置。"

# game/tutorial_atl.rpy:216
translate zh_cn tutorial_positions_8e7d3e52:

    # e "When we're positioning something, the area is usually the entire screen."
    e "定位元素时，该区域通常是整个屏幕。"

# game/tutorial_atl.rpy:218
translate zh_cn tutorial_positions_fdcf9d8b:

    # e "Let me get out of the way, and I'll show you where some positions are."
    e "我让开位置，给你展示几个坐标点的位置。"

# game/tutorial_atl.rpy:232
translate zh_cn tutorial_positions_76d7a5bf:

    # e "The origin is the upper-left corner of the screen. That's where the x position (xpos) and the y position (ypos) are both zero."
    e "原点位于屏幕左上角，此处x坐标(xpos)和y坐标(ypos)均为零。"

# game/tutorial_atl.rpy:238
translate zh_cn tutorial_positions_be14c7c3:

    # e "When we increase xpos, we move to the right. So here's an xpos of .5, meaning half the width across the screen."
    e "增加xpos会向右移动。这里xpos是.5，表示屏幕宽度的一半位置。"

# game/tutorial_atl.rpy:243
translate zh_cn tutorial_positions_9b91be6c:

    # e "Increasing xpos to 1.0 moves us to the right-hand border of the screen."
    e "将xpos增至1.0会移动到屏幕右边界。"

# game/tutorial_atl.rpy:249
translate zh_cn tutorial_positions_2b293304:

    # e "We can also use an absolute xpos, which is given in an absolute number of pixels from the left side of the screen. For example, since this window is 1280 pixels across, using an xpos of 640 will return the target to the center of the top row."
    e "也可使用绝对xpos（以像素为单位）。例如本窗口宽1280像素，xpos设为640将使目标回到顶部行中心。"

# game/tutorial_atl.rpy:251
translate zh_cn tutorial_positions_c4d18c0a:

    # e "The y-axis position, or ypos works the same way. Right now, we have a ypos of 0.0."
    e "y轴坐标(ypos)同理。当前ypos为0.0。"

# game/tutorial_atl.rpy:257
translate zh_cn tutorial_positions_16933a61:

    # e "Here's a ypos of 0.5."
    e "这是ypos=0.5的位置。"

# game/tutorial_atl.rpy:262
translate zh_cn tutorial_positions_6eb36777:

    # e "A ypos of 1.0 specifies a position at the bottom of the screen. If you look carefully, you can see the position indicator spinning below the text window."
    e "ypos=1.0定位到屏幕底部。仔细观察可看到定位指示器在文本窗下方旋转。"

# game/tutorial_atl.rpy:264
translate zh_cn tutorial_positions_a423050f:

    # e "Like xpos, ypos can also be an integer. In this case, ypos would give the total number of pixels from the top of the screen."
    e "与xpos类似，ypos也可以是整数（表示距屏幕顶部的像素值）。"

# game/tutorial_atl.rpy:272
translate zh_cn tutorial_positions_bc7a809a:

    # e "Can you guess where this position is, relative to the screen?" nointeract
    e "你能猜出这个位置相对于屏幕的坐标吗？" nointeract

# game/tutorial_atl.rpy:276
translate zh_cn tutorial_positions_6f926e18:

    # e "Sorry, that's wrong. The xpos is .75, and the ypos is .25."
    e "抱歉，错误。xpos是.75，ypos是.25。"

# game/tutorial_atl.rpy:278
translate zh_cn tutorial_positions_5d5feb98:

    # e "In other words, it's 75%% of the way from the left side, and 25%% of the way from the top."
    e "即从左侧起75%距离，顶部起25%距离。"

# game/tutorial_atl.rpy:282
translate zh_cn tutorial_positions_77b45218:

    # e "Good job! You got that position right."
    e "做得好！这个位置猜对了。"

# game/tutorial_atl.rpy:286
translate zh_cn tutorial_positions_6f926e18_1:

    # e "Sorry, that's wrong. The xpos is .75, and the ypos is .25."
    e "抱歉，错误。xpos是.75，ypos是.25。"

# game/tutorial_atl.rpy:288
translate zh_cn tutorial_positions_5d5feb98_1:

    # e "In other words, it's 75%% of the way from the left side, and 25%% of the way from the top."
    e "即从左侧起75%距离，顶部起25%距离。"

# game/tutorial_atl.rpy:302
translate zh_cn tutorial_positions_e4380a83:

    # e "The second position we care about is the anchor. The anchor is a spot on the thing being positioned."
    e "第二个关键点是锚点(anchor)，即被定位元素本身的参考点。"

# game/tutorial_atl.rpy:304
translate zh_cn tutorial_positions_d1db1246:

    # e "For example, here we have an xanchor of 0.0 and a yanchor of 0.0. It's in the upper-left corner of the logo image."
    e "例如这里xanchor=0.0且yanchor=0.0，锚点在Logo图像的左上角。"

# game/tutorial_atl.rpy:309
translate zh_cn tutorial_positions_6056873f:

    # e "When we increase the xanchor to 1.0, the anchor moves to the right corner of the image."
    e "当xanchor增至1.0，锚点移至图像右侧。"

# game/tutorial_atl.rpy:314
translate zh_cn tutorial_positions_7cdb8dcc:

    # e "Similarly, when both xanchor and yanchor are 1.0, the anchor is the bottom-right corner."
    e "同理当xanchor和yanchor均为1.0时，锚点在右下角。"

# game/tutorial_atl.rpy:321
translate zh_cn tutorial_positions_03a07da8:

    # e "To place an image on the screen, we need both the position and the anchor."
    e "定位图像需要同时指定位置(position)和锚点(anchor)。"

# game/tutorial_atl.rpy:329
translate zh_cn tutorial_positions_8945054f:

    # e "We then line them up, so that both the position and anchor are at the same point on the screen."
    e "我们将它们对齐，使位置点和锚点重合于屏幕同一点。"

# game/tutorial_atl.rpy:339
translate zh_cn tutorial_positions_2b184a93:

    # e "When we place both in the upper-left corner, the image moves to the upper-left corner of the screen."
    e "当两者都在左上角时，图像移至屏幕左上角。"

# game/tutorial_atl.rpy:348
translate zh_cn tutorial_positions_5aac4f3f:

    # e "With the right combination of position and anchor, any place on the screen can be specified, without even knowing the size of the image."
    e "通过位置和锚点的组合，无需知道图像尺寸即可定位到屏幕任意位置。"

# game/tutorial_atl.rpy:360
translate zh_cn tutorial_positions_3b59b797:

    # e "It's often useful to set xpos and xanchor to the same value. We call that xalign, and it gives a fractional position on the screen."
    e "将xpos与xanchor设为相同值通常很实用，这称为xalign（水平对齐）。"

# game/tutorial_atl.rpy:365
translate zh_cn tutorial_positions_b8ebf9fe:

    # e "For example, when we set xalign to 0.0, things are aligned to the left side of the screen."
    e "例如xalign=0.0时元素左对齐。"

# game/tutorial_atl.rpy:370
translate zh_cn tutorial_positions_8ce35d52:

    # e "When we set it to 1.0, then we're aligned to the right side of the screen."
    e "设为1.0时右对齐。"

# game/tutorial_atl.rpy:375
translate zh_cn tutorial_positions_6745825f:

    # e "And when we set it to 0.5, we're back to the center of the screen."
    e "设为0.5时回到屏幕水平中心。"

# game/tutorial_atl.rpy:377
translate zh_cn tutorial_positions_64428a07:

    # e "Setting yalign is similar, except along the y-axis."
    e "yalign同理（控制垂直对齐）。"

# game/tutorial_atl.rpy:379
translate zh_cn tutorial_positions_cfb77d42:

    # e "Remember that xalign is just setting xpos and xanchor to the same value, and yalign is just setting ypos and yanchor to the same value."
    e "记住：xalign本质是设置xpos与xanchor同值，yalign同理。"

# game/tutorial_atl.rpy:384
translate zh_cn tutorial_positions_cfc1723e:

    # e "The xcenter and ycenter properties position the center of the image. Here, with xcenter set to .75, the center of the image is three-quarters of the way to the right side of the screen."
    e "xcenter/ycenter属性定位图像中心。此处xcenter=.75，图像中心位于屏幕右侧3/4处。"

# game/tutorial_atl.rpy:389
translate zh_cn tutorial_positions_7728dbf9:

    # e "The difference between xalign and xcenter is more obvious when xcenter is 1.0, and the image is halfway off the right side of the screen."
    e "当xcenter=1.0时（图像右侧一半移出屏幕），xalign与xcenter的差异更明显。"

# game/tutorial_atl.rpy:397
translate zh_cn tutorial_positions_1b1cedc6:

    # e "There are the xoffset and yoffset properties, which are applied after everything else, and offset things to the right or bottom, respectively."
    e "xoffset/yoffset属性在所有定位后生效，分别向右/下方偏移。"

# game/tutorial_atl.rpy:402
translate zh_cn tutorial_positions_e6da2798:

    # e "Of course, you can use negative numbers to offset things to the left and top."
    e "当然可用负数实现向左/上方偏移。"

# game/tutorial_atl.rpy:407
translate zh_cn tutorial_positions_e0fe2d81:

    # e "Lastly, I'll mention that there are combined properties like align, pos, anchor, and center. Align takes a pair of numbers, and sets xalign to the first and yalign to the second. The others are similar."
    e "最后介绍组合属性：align（对齐）、pos（位置）、anchor（锚点）、center（中心）。align接收两个数字，分别设置xalign/yalign。其他属性同理。"

# game/tutorial_atl.rpy:414
translate zh_cn tutorial_positions_0f4ca2b6:

    # e "Once you understand positions, you can use transformations to move things around the Ren'Py screen."
    e "理解定位后，就能用变换(transform)在Ren'Py屏幕上移动元素了。"

# game/tutorial_atl.rpy:421
translate zh_cn tutorial_atl_d5d6b62a:

    # e "Ren'Py uses transforms to animate, manipulate, and place images. We've already seen the very simplest of transforms in use:"
    e "Ren'Py用变换实现动画、操控和定位。我们已经见过最简单的变换："

# game/tutorial_atl.rpy:428
translate zh_cn tutorial_atl_7e853c9d:

    # e "Transforms can be very simple affairs that place the image somewhere on the screen, like the right transform."
    e "变换可以简单到仅定位图像（如right变换）。"

# game/tutorial_atl.rpy:432
translate zh_cn tutorial_atl_87a6ecbd:

    # e "But transforms can also be far more complicated affairs, that introduce animation and effects into the mix. To demonstrate, let's have a Gratuitous Rock Concert!"
    e "但变换也能实现复杂动画特效。下面演示一场奢华摇滚音乐会！"

# game/tutorial_atl.rpy:440
translate zh_cn tutorial_atl_65badef3:

    # e "But first, let's have... a Gratuitous Rock Concert!"
    e "不过首先...来场奢华摇滚音乐会！"

# game/tutorial_atl.rpy:448
translate zh_cn tutorial_atl_e0d3c5ec:

    # e "That was a lot of work, but it was built out of small parts."
    e "工程虽大，但由小模块构建而成。"

# game/tutorial_atl.rpy:450
translate zh_cn tutorial_atl_f2407514:

    # e "Most transforms in Ren'Py are built using the Animation and Transform Language, or ATL for short."
    e "Ren'Py多数变换通过动画变换语言(ATL)构建。"

# game/tutorial_atl.rpy:452
translate zh_cn tutorial_atl_1f22f875:

    # e "There are currently three places where ATL can be used in Ren'Py."
    e "目前ATL在Ren'Py中有三处应用场景："

# game/tutorial_atl.rpy:457
translate zh_cn tutorial_atl_fd036bdf:

    # e "The first place ATL can be used is as part of an image statement. Instead of a displayable, an image may be defined as a block of ATL code."
    e "第一是image语句中。图像可定义为ATL代码块而非可视组件(displayable)。"

# game/tutorial_atl.rpy:459
translate zh_cn tutorial_atl_7cad2ab9:

    # e "When used in this way, we have to be sure that ATL includes one or more displayables to actually show."
    e "此用法需确保ATL包含至少一个可视组件。"

# game/tutorial_atl.rpy:464
translate zh_cn tutorial_atl_c78b2a1e:

    # e "The second way is through the use of the transform statement. This assigns the ATL block to a python variable, allowing it to be used in at clauses and inside other transforms."
    e "第二是transform语句。将ATL代码块赋给Python变量，用于at子句或其他变换内部。"

# game/tutorial_atl.rpy:476
translate zh_cn tutorial_atl_da7a7759:

    # e "Finally, an ATL block can be used as part of a show statement, instead of the at clause." id tutorial_atl_da7a7759
    e "第三是在show语句中替代at子句直接使用ATL块。" id tutorial_atl_da7a7759

# game/tutorial_atl.rpy:483
translate zh_cn tutorial_atl_1dd345c6:

    # e "When ATL is used as part of a show statement, values of properties exist even when the transform is changed. So even though your click stopped the motion, the image remains in the same place." id tutorial_atl_1dd345c6
    e "在show语句中使用ATL时，属性值在变换更改后仍会保留。即使点击停止运动，图像仍停在原位。" id tutorial_atl_1dd345c6

# game/tutorial_atl.rpy:491
translate zh_cn tutorial_atl_98047789:

    # e "The key to ATL is what we call composability. ATL is made up of relatively simple commands, which can be combined together to create complicated transforms."
    e "ATL核心在于可组合性(composability)。它由简单命令组成，可组合创建复杂变换。"

# game/tutorial_atl.rpy:493
translate zh_cn tutorial_atl_ed82983f:

    # e "Before I explain how ATL works, let me explain what animation and transformation are."
    e "讲解ATL前，先说明动画(animation)与变换(transformation)的区别："

# game/tutorial_atl.rpy:498
translate zh_cn tutorial_atl_2807adff:

    # e "Animation is when the displayable being shown changes. For example, right now I am changing my expression."
    e "动画改变显示内容（例如我现在的表情变化）。"

# game/tutorial_atl.rpy:525
translate zh_cn tutorial_atl_3eec202b:

    # e "Transformation involves moving or distorting an image. This includes placing it on the screen, zooming it in and out, rotating it, and changing its opacity."
    e "变换指移动或扭曲图像（包括定位、缩放、旋转、透明度变化）。"

# game/tutorial_atl.rpy:533
translate zh_cn tutorial_atl_fbc9bf83:

    # e "To introduce ATL, let's start by looking at a simple animation. Here's one that consists of five lines of ATL code, contained within an image statement." id tutorial_atl_fbc9bf83
    e "通过简单动画引入ATL：这个包含5行ATL代码的image语句示例。" id tutorial_atl_fbc9bf83

# game/tutorial_atl.rpy:535
translate zh_cn tutorial_atl_bf92d973:

    # e "To change a displayable, simply mention it on a line of ATL. Here, we're switching back and forth between two images."
    e "要切换可视组件，只需在ATL行中声明它（这里交替显示两个图像）。"

# game/tutorial_atl.rpy:537
translate zh_cn tutorial_atl_51a41db4:

    # e "Since we're defining an image, the first line of ATL must give a displayable. Otherwise, there would be nothing to show."
    e "定义图像时，ATL首行必须声明可视组件（否则无内容显示）。"

# game/tutorial_atl.rpy:539
translate zh_cn tutorial_atl_3d065074:

    # e "The second and fourth lines are pause statements, which cause ATL to wait half a second each before continuing. That's how we give the delay between images."
    e "第二、四行是pause语句（使ATL每次等待半秒），形成图像切换间隔。"

# game/tutorial_atl.rpy:541
translate zh_cn tutorial_atl_60f2a5e8:

    # e "The final line is a repeat statement. This causes the current block of ATL to be restarted. You can only have one repeat statement per block."
    e "最后是repeat语句（使当前ATL块循环）。每个块只能有一个repeat语句。"

# game/tutorial_atl.rpy:546
translate zh_cn tutorial_atl_146cf4c4:

    # e "If we were to write repeat 2 instead, the animation would loop twice, then stop."
    e "若写repeat 2，动画循环两次后停止。"

# game/tutorial_atl.rpy:551
translate zh_cn tutorial_atl_d90b1838:

    # e "Omitting the repeat statement means that the animation stops once we reach the end of the block of ATL code."
    e "省略repeat语句则动画执行到ATL块末尾即停止。"

# game/tutorial_atl.rpy:556
translate zh_cn tutorial_atl_e5872360:

    # e "By default, displayables are replaced instantaneously. We can also use a with clause to give a transition between displayables."
    e "默认切换是瞬时的。可用with子句添加转场效果。"

# game/tutorial_atl.rpy:563
translate zh_cn tutorial_atl_2e9d63ea:

    # e "With animation done, we'll see how we can use ATL to transform images, starting with positioning an image on the screen."
    e "了解动画后，再看ATL如何变换图像（从定位开始）。"

# game/tutorial_atl.rpy:572
translate zh_cn tutorial_atl_ddc55039:

    # e "The simplest thing we can do is to statically position an image. This is done by giving the names of the position properties, followed by the property values." id tutorial_atl_ddc55039
    e "最简单是静态定位：直接声明定位属性及值。" id tutorial_atl_ddc55039

# game/tutorial_atl.rpy:577
translate zh_cn tutorial_atl_43516492:

    # e "With a few more statements, we can move things around on the screen."
    e "添加语句可实现屏幕移动："

# game/tutorial_atl.rpy:579
translate zh_cn tutorial_atl_fb979287:

    # e "This example starts the image off at the top-right of the screen, and waits a second. It then moves it to the left side, waits another second, and repeats."
    e "此示例让图像从右上角开始，等待1秒后移至左侧，再等1秒后循环。"

# game/tutorial_atl.rpy:581
translate zh_cn tutorial_atl_7650ec09:

    # e "The pause and repeat statements are the same statements we used in our animations. They work throughout ATL code."
    e "pause/repeat语句与动画中用法一致（在整个ATL中通用）。"

# game/tutorial_atl.rpy:586
translate zh_cn tutorial_atl_d3416d4f:

    # e "Having the image jump around on the screen isn't all that useful. That's why ATL has the interpolation statement."
    e "单纯跳跃移动不实用，因此ATL提供插值语句(interpolation statement)："

# game/tutorial_atl.rpy:588
translate zh_cn tutorial_atl_4e7512ec:

    # e "The interpolation statement allows you to smoothly vary the value of a transform property, from an old to a new value."
    e "插值语句可平滑改变变换属性值（从旧值过渡到新值）。"

# game/tutorial_atl.rpy:590
translate zh_cn tutorial_atl_685eeeaa:

    # e "Here, we have an interpolation statement on the second ATL line. It starts off with the name of a time function, in this case linear."
    e "第二个ATL行是插值语句：以时间函数（如linear）开头，"

# game/tutorial_atl.rpy:592
translate zh_cn tutorial_atl_c5cb49de:

    # e "That's followed by an amount of time, in this case three seconds. It ends with a list of properties, each followed by its new value."
    e "后接时长（如3秒），最后是属性及其目标值列表。"

# game/tutorial_atl.rpy:594
translate zh_cn tutorial_atl_04b8bc1d:

    # e "The value of each property is interpolated from its value when the statement starts to the value at the end of the statement. This is done once per frame, allowing smooth animation."
    e "每个属性值从语句起始值渐变到目标值（每帧更新实现平滑动画）。"

# game/tutorial_atl.rpy:605
translate zh_cn tutorial_atl_2958f397:

    # e "ATL supports more complicated move types, like circle and spline motion. But I won't be showing those here."
    e "ATL支持更复杂运动（如圆形/样条曲线），但此处不演示。"

# game/tutorial_atl.rpy:609
translate zh_cn tutorial_atl_d08fe8d9:

    # e "Apart from displayables, pause, interpolation, and repeat, there are a few other statements we can use as part of ATL."
    e "除可视组件、pause、插值和repeat外，ATL还有其他语句："

# game/tutorial_atl.rpy:621
translate zh_cn tutorial_atl_84b22ac0:

    # e "ATL transforms created using the statement become ATL statements themselves. Since the default positions are also transforms, this means that we can use left, right, and center inside of an ATL block."
    e "transform语句创建的变换本身可作为ATL语句使用（默认位置也是变换），因此ATL块内可直接使用left/right/center。"

# game/tutorial_atl.rpy:637
translate zh_cn tutorial_atl_331126c1:

    # e "Here, we have two new statements. The block statement allows you to include a block of ATL code. Since the repeat statement applies to blocks, this lets you repeat only part of an ATL transform."
    e "这里有两个新语句：block语句包含ATL子块（repeat仅作用于当前块）；"

# game/tutorial_atl.rpy:639
translate zh_cn tutorial_atl_24f67b67:

    # e "We also have the time statement, which runs after the given number of seconds have elapsed from the start of the block. It will run even if another statement is running, stopping the other statement."
    e "time语句在指定秒数后触发（即使其他语句正在运行也会中断它们）。"

# game/tutorial_atl.rpy:641
translate zh_cn tutorial_atl_b7709507:

    # e "So this example bounces the image back and forth for eleven and a half seconds, and then moves it to the right side of the screen."
    e "此例让图像弹跳11.5秒后移至屏幕右侧。"

# game/tutorial_atl.rpy:655
translate zh_cn tutorial_atl_f903bc3b:

    # e "The parallel statement lets us run two blocks of ATL code at the same time."
    e "parallel语句可并行运行两个ATL块："

# game/tutorial_atl.rpy:657
translate zh_cn tutorial_atl_5d0f8f9d:

    # e "Here, the top block move the image in the horizontal direction, and the bottom block moves it in the vertical direction. Since they're moving at different speeds, it looks like the image is bouncing on the screen."
    e "上方块控制水平移动，下方块控制垂直移动（因速度不同形成弹跳效果）。"

# game/tutorial_atl.rpy:671
translate zh_cn tutorial_atl_28a7d27e:

    # e "Finally, the choice statement makes Ren'Py randomly pick a block of ATL code. This allows you to add some variation as to what Ren'Py shows."
    e "choice语句让Ren'Py随机选择ATL块执行（增加显示内容的随机性）。"

# game/tutorial_atl.rpy:677
translate zh_cn tutorial_atl_2265254b:

    # e "This tutorial game has only scratched the surface of what you can do with ATL. For example, we haven't even covered the on and event statements. For more information, you might want to check out {a=https://renpy.org/doc/html/atl.html}the ATL chapter in the reference manual{/a}."
    e "本教程仅浅析ATL功能（未涵盖on/event语句）。更多信息请查阅{a=https://renpy.org/doc/html/atl.html}参考手册ATL章节{/a}。"

# game/tutorial_atl.rpy:686
translate zh_cn transform_properties_391169cf:

    # e "Ren'Py has quite a few transform properties that can be used with ATL, the Transform displayable, and the add Screen Language statement."
    e "Ren'Py有许多可用于ATL、Transform可视组件和add屏幕语句的变换属性。"

# game/tutorial_atl.rpy:687
translate zh_cn transform_properties_fc895a1f:

    # e "Here, we'll show them off so you can see them in action and get used to what each does."
    e "下面展示这些属性，助你熟悉其效果："

# game/tutorial_atl.rpy:703
translate zh_cn transform_properties_88daf990:

    # e "First off, all of the position properties are also transform properties. These include the pos, anchor, align, center, and offset properties."
    e "首先，所有定位属性都可作为变换属性（包括pos, anchor, align, center, offset）。"

# game/tutorial_atl.rpy:721
translate zh_cn transform_properties_d7a487f1:

    # e "The position properties can also be used to pan over a displayable larger than the screen, by giving xpos and ypos negative values."
    e "通过给xpos/ypos赋负值，还可平移大于屏幕的可视组件。"

# game/tutorial_atl.rpy:731
translate zh_cn transform_properties_89e0d7c2:

    # "The subpixel property controls how things are lined up with the screen. When False, images can be pixel-perfect, but there can be pixel jumping."
    "subpixel属性控制屏幕对齐方式：False时图像像素精准但可能跳跃；"

# game/tutorial_atl.rpy:738
translate zh_cn transform_properties_4194527e:

    # "When it's set to True, movement is smoother at the cost of blurring images a little."
    "True时移动更平滑（但略有模糊）。"

# game/tutorial_atl.rpy:757
translate zh_cn transform_properties_35934e77:

    # e "Transforms also support polar coordinates. The around property sets the center of the coordinate system to coordinates given in pixels."
    e "变换还支持极坐标：around属性设置坐标系中心（像素坐标）；"

# game/tutorial_atl.rpy:765
translate zh_cn transform_properties_605ebd0c:

    # e "The angle property gives the angle in degrees. Angles run clockwise, with the zero angle at the top of the screen."
    e "angle属性设置角度（度为单位，顺时针方向，屏幕顶部为0度）；"

# game/tutorial_atl.rpy:774
translate zh_cn transform_properties_6d4555ed:

    # e "The radius property gives the distance in pixels from the anchor of the displayable to the center of the coordinate system."
    e "radius属性设置可视组件锚点到坐标系中心的距离（像素）。"

# game/tutorial_atl.rpy:788
translate zh_cn transform_properties_7af037a5:

    # e "There are several ways to resize a displayable. The zoom property lets us scale a displayable by a factor, making it bigger and smaller."
    e "缩放可视组件有多种方式：zoom属性按比例缩放；"

# game/tutorial_atl.rpy:801
translate zh_cn transform_properties_b6527546:

    # e "The xzoom and yzoom properties allow the displayable to be scaled in the X and Y directions independently."
    e "xzoom/yzoom属性支持X/Y轴独立缩放；"

# game/tutorial_atl.rpy:811
translate zh_cn transform_properties_b98b780b:

    # e "By making xzoom or yzoom a negative number, we can flip the image horizontally or vertically."
    e "将xzoom/yzoom设为负数可实现水平/垂直翻转；"

# game/tutorial_atl.rpy:821
translate zh_cn transform_properties_74d542ff:

    # e "Instead of zooming by a scale factor, the size transform property can be used to scale a displayable to a size in pixels."
    e "size属性可直接设置像素尺寸（替代比例缩放）。"

# game/tutorial_atl.rpy:836
translate zh_cn transform_properties_438ed776:

    # e "The alpha property is used to change the opacity of a displayable. This can make it appear and disappear."
    e "alpha属性改变透明度（实现淡入淡出）；"

# game/tutorial_atl.rpy:849
translate zh_cn transform_properties_aee19f86:

    # e "The rotate property rotates a displayable."
    e "rotate属性旋转可视组件；"

# game/tutorial_atl.rpy:860
translate zh_cn transform_properties_57b3235a:

    # e "By default, when a displayable is rotated, Ren'Py will include extra space on all four sides, so the size doesn't change as it rotates. Here, you can see the extra space on the left and top, and it's also there on the right and bottom."
    e "默认旋转时Ren'Py会预留四边空间（保持尺寸不变）。此处可见左上及右下留白；"

# game/tutorial_atl.rpy:872
translate zh_cn transform_properties_66d29ee8:

    # e "By setting rotate_pad to False, we can get rid of the space, at the cost of the size of the displayable changing as it rotates."
    e "设置rotate_pad=False可取消留白（但旋转时尺寸会变化）。"

# game/tutorial_atl.rpy:883
translate zh_cn transform_properties_7f32e8ad:

    # e "The tile transform properties, xtile and ytile, repeat the displayable multiple times."
    e "xtile/ytile属性平铺重复可视组件；"

# game/tutorial_atl.rpy:893
translate zh_cn transform_properties_207b7fc8:

    # e "The crop property crops a rectangle out of a displayable, showing only part of it."
    e "crop属性裁剪可视组件（仅显示部分区域）；"

# game/tutorial_atl.rpy:907
translate zh_cn transform_properties_e7e22d28:

    # e "When used together, crop and size can be used to focus in on specific parts of an image."
    e "crop与size结合可聚焦图像特定区域；"

# game/tutorial_atl.rpy:919
translate zh_cn transform_properties_f34abd82:

    # e "The xpan and ypan properties can be used to pan over a displayable, given an angle in degrees, with 0 being the center."
    e "xpan/ypan属性按角度平移可视组件（0度表示中心位置）。"

# game/tutorial_atl.rpy:926
translate zh_cn transform_properties_bfa3b139:

    # e "Those are all the transform properties we have to work with. By putting them together in the right order, you can create complex things."
    e "以上就是所有变换属性。通过合理组合可创造复杂效果。"

translate zh_cn strings:

    # game/tutorial_atl.rpy:270
    old "xpos 1.0 ypos .5"
    new "xpos 1.0 ypos .5"

    # game/tutorial_atl.rpy:270
    old "xpos .75 ypos .25"
    new "xpos .75 ypos .25"

    # game/tutorial_atl.rpy:270
    old "xpos .25 ypos .33"
    new "xpos .25 ypos .33"

