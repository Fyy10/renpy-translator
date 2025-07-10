# TODO: Translation updated at 2025-07-09 16:06

# game/indepth_style.rpy:40
translate zh_cn new_gui_17a0326e:

    # e "When you create a new project, Ren'Py will automatically create a GUI - a Graphical User Interface - for it."
    e "当你创建新项目时，Ren'Py会自动为其生成GUI——即图形用户界面。"

# game/indepth_style.rpy:42
translate zh_cn new_gui_12c814ed:

    # e "It defines the look of both in-game interface, like this text box, and out-of-game interface like the main and game menus."
    e "它同时定义了游戏内界面（如这个文本框）和游戏外界面（如主菜单和游戏菜单）的外观。"

# game/indepth_style.rpy:44
translate zh_cn new_gui_0a2a73bb:

    # e "The default GUI is meant to be nice enough for a simple project. With a few small changes, it's what you're seeing in this game."
    e "默认GUI足以满足简单项目的需求。只需稍作修改，就是你现在在本游戏中看到的界面。"

# game/indepth_style.rpy:46
translate zh_cn new_gui_22adf68e:

    # e "The GUI is also meant to be easy for an intermediate creator to customize. Customizing the GUI consists of changing the image files in the gui directory, and changing variables in gui.rpy."
    e "该GUI也便于中级创作者自定义。自定义GUI包括替换gui目录中的图像文件，以及修改gui.rpy中的变量。"

# game/indepth_style.rpy:48
translate zh_cn new_gui_da21de30:

    # e "At the same time, even when customized, the default GUI might be too recognizable for an extremely polished game. That's why we've made it easy to totally replace."
    e "同时，即使经过自定义，默认GUI对于高度精良的游戏可能仍过于眼熟。因此我们设计了可彻底替换的机制。"

# game/indepth_style.rpy:50
translate zh_cn new_gui_45765574:

    # e "We've put an extensive guide to customizing the GUI on the Ren'Py website. So if you want to learn more, visit the {a=https://www.renpy.org/doc/html/gui.html}GUI customization guide{/a}."
    e "我们在Ren'Py官网上放置了详尽的GUI定制指南。若想深入了解，请访问{a=https://www.renpy.org/doc/html/gui.html}GUI定制指南{/a}。"

# game/indepth_style.rpy:58
translate zh_cn styles_fa345a38:

    # e "Ren'Py has a powerful style system that controls what displayables look like."
    e "Ren'Py拥有强大的样式系统，用于控制可视组件的外观。"

# game/indepth_style.rpy:60
translate zh_cn styles_6189ee12:

    # e "While the default GUI uses variables to provide styles with sensible defaults, if you're replacing the GUI or creating your own screens, you'll need to learn about styles yourself."
    e "虽然默认GUI使用变量提供合理的预设样式，但若要替换GUI或创建自定义界面，你需要自行学习样式系统。"

# game/indepth_style.rpy:68
translate zh_cn styles_menu_a4a6913e:

    # e "What would you like to know about styles?" nointeract
    e "你想了解关于样式的哪些内容？" nointeract

# game/indepth_style.rpy:98
translate zh_cn style_basics_9a79ef89:

    # e "Styles let a displayable look different from game to game, or even inside the same game."
    e "样式使同一可视组件在不同游戏甚至同款游戏中呈现不同外观。"

# game/indepth_style.rpy:103
translate zh_cn style_basics_48777f2c:

    # e "Both of these buttons use the same displayables. But since different styles have been applied, the buttons look different from each other."
    e "这两个按钮使用相同的可视组件。但因应用了不同样式，按钮外观截然不同。"

# game/indepth_style.rpy:108
translate zh_cn style_basics_57704d8c:

    # e "Styles are a combination of information from four different places."
    e "样式由四个不同来源的信息组合而成。"

# game/indepth_style.rpy:121
translate zh_cn style_basics_144731f6:

    # e "The first place Ren'Py can get style information from is part of a screen. Each displayable created by a screen can take a style name and style properties."
    e "Ren'Py获取样式信息的首要来源是界面内部。由界面创建的每个可视组件都可接收样式名称和样式属性。"

# game/indepth_style.rpy:138
translate zh_cn style_basics_67e48162:

    # e "When a screen displayable contains text, style properties prefixed with text_ apply to that text."
    e "当界面可视组件包含文本时，以text_为前缀的样式属性将应用于该文本。"

# game/indepth_style.rpy:151
translate zh_cn style_basics_03516b4a:

    # e "The next is as part of a displayable created in an image statement. Style properties are just arguments to the displayable."
    e "其次来自图像语句创建的可视组件。样式属性即该可视组件的参数。"

# game/indepth_style.rpy:160
translate zh_cn style_basics_ccc0d1ca:

    # egreen "Style properties can also be given as arguments when defining a character."
    egreen "定义角色时也可将样式属性作为参数传递。"

# game/indepth_style.rpy:162
translate zh_cn style_basics_013ab314:

    # egreen "Arguments beginning with who_ are style properties applied to the character's name, while those beginning with what_ are applied to the character's dialogue."
    egreen "以who_开头的参数是应用于角色名称的样式属性，以what_开头的则应用于角色对话。"

# game/indepth_style.rpy:164
translate zh_cn style_basics_dbe80939:

    # egreen "Style properties that don't have a prefix are also applied to the character's name."
    egreen "无前缀的样式属性同样应用于角色名称。"

# game/indepth_style.rpy:174
translate zh_cn style_basics_ac6a8414:

    # e "Finally, there is the style statement, which creates or changes a named style. By giving Text the style argument, we tell it to use the blue_text style." id style_basics_ac6a8414
    e "最后是style语句，它创建或修改命名样式。通过给Text传递style参数，我们使其使用blue_text样式。" id style_basics_ac6a8414

# game/indepth_style.rpy:180
translate zh_cn style_basics_3d9bdff7:

    # e "A style property can inherit from a parent. If a style property is not given in a style, it comes from the parent of that style."
    e "样式属性可从父级继承。若某样式未定义属性，则从其父样式继承。"

# game/indepth_style.rpy:182
translate zh_cn style_basics_49c5fbfe:

    # e "By default the parent of the style has the same name, with the prefix up to the first underscore removed. If the style does not have an underscore in its name, 'default' is used." id style_basics_49c5fbfe
    e "默认情况下，父样式的名称是去除首个下划线前前缀的本名。若无下划线，则继承'default'样式。" id style_basics_49c5fbfe

# game/indepth_style.rpy:184
translate zh_cn style_basics_6ab170a3:

    # e "For example, blue_text inherits from text, which in turn inherits from default. The default style defines all properties, so it doesn't inherit from anything."
    e "例如blue_text继承自text，而text又继承自default。default样式定义所有属性，故无继承源。"

# game/indepth_style.rpy:190
translate zh_cn style_basics_f78117a7:

    # e "The parent can be explicitly changed by giving the style statement an 'is' clause. In this case, we're explictly setting the style to the parent of text."
    e "通过给style语句添加'is'从句可显式更改父级。此例中我们显式设置父级为text的父样式。"

# game/indepth_style.rpy:194
translate zh_cn style_basics_6007040b:

    # e "Each displayable has a default style name. By default, it's usually the lower-case displayable name, like 'text' for Text, or 'button' for buttons."
    e "每个可视组件都有默认样式名。通常是小写的组件名称，如Text对应'text'，按钮对应'button'。"

# game/indepth_style.rpy:196
translate zh_cn style_basics_35db9a05:

    # e "In a screen, a displayable can be given the style_prefix property to give a prefix for that displayable and its children." id style_basics_35db9a05
    e "界面中可通过style_prefix属性为可视组件及其子项添加样式前缀。" id style_basics_35db9a05

# game/indepth_style.rpy:198
translate zh_cn style_basics_422a87f7:

    # e "For example, a text displayable with a style_prefix of 'help' will be given the style 'help_text'."
    e "例如，带'help'前缀的文本可视组件将应用'help_text'样式。"

# game/indepth_style.rpy:200
translate zh_cn style_basics_bad2e207:

    # e "Lastly, when a displayable is a button, or inside a button, it can take style prefixes."
    e "最后，当可视组件是按钮或位于按钮内部时，可接收样式前缀。"

# game/indepth_style.rpy:202
translate zh_cn style_basics_22ed20a1:

    # e "The prefixes idle_, hover_, and insensitive_ are used when the button is unfocused, focused, and unfocusable."
    e "前缀idle_、hover_和insensitive_分别用于按钮未聚焦、聚焦和不可聚焦状态。"

# game/indepth_style.rpy:204
translate zh_cn style_basics_7a58037e:

    # e "These can be preceded by selected_ to change how the button looks when it represents a selected value or screen."
    e "这些前缀可附加selected_前缀，以改变按钮代表选中值或界面时的外观。"

# game/indepth_style.rpy:233
translate zh_cn style_basics_0cdcb8c3:

    # e "This screen shows the style prefixes in action. You can click on a button to select it, or click outside to advance."
    e "本界面展示了实际应用的样式前缀。点击按钮进行选择，或点击外部区域继续。"

# game/indepth_style.rpy:240
translate zh_cn style_basics_aed05094:

    # e "Those are the basics of styles. If GUI customization isn't enough for you, styles let you customize just about everything in Ren'Py."
    e "以上是样式基础。若GUI自定义无法满足需求，样式系统可让你定制Ren'Py几乎所有元素。"

# game/indepth_style.rpy:253
translate zh_cn style_general_81f3c8ff:

    # e "The first group of style properties that we'll go over are the general style properties. These work with every displayable, or at least many different ones."
    e "我们将介绍的第一组样式属性是通用属性。这些属性适用于所有或多数可视组件。"

# game/indepth_style.rpy:264
translate zh_cn style_general_a8d99699:

    # e "Every displayable takes the position properties, which control where it can be placed on screen. Since I've already mentioned them, I won't repeat them here."
    e "每个可视组件都接收控制其屏幕位置的位置属性。因前文已提及，此处不再赘述。"

# game/indepth_style.rpy:275
translate zh_cn style_general_58d4a18f:

    # e "The xmaximum and ymaximum properties set the maximum width and height of the displayable, respectively. This will cause Ren'Py to shrink things, if possible."
    e "xmaximum和ymaximum属性分别设置可视组件的最大宽度和高度。这将使Ren'Py尽可能收缩元素。"

# game/indepth_style.rpy:277
translate zh_cn style_general_cae9a39f:

    # e "Sometimes, the shrunken size will be smaller than the size given by xmaximum and ymaximum."
    e "有时收缩后的尺寸会小于xmaximum和ymaximum的设定值。"

# game/indepth_style.rpy:279
translate zh_cn style_general_5928c24e:

    # e "Similarly, the xminimum and yminimum properties set the minimum width and height. If the displayable is smaller, Ren'Py will try to make it bigger."
    e "类似地，xminimum和yminimum属性设置最小宽高。若可视组件更小，Ren'Py会尝试扩展它。"

# game/indepth_style.rpy:289
translate zh_cn style_general_35a8ee5e:

    # e "The xsize and ysize properties set the minimum and maximum size to the same value, fixing the size."
    e "xsize和ysize属性将最小/最大尺寸设为相同值以固定尺寸。"

# game/indepth_style.rpy:291
translate zh_cn style_general_fcfb0640:

    # e "These only works for displayables than can be resized. Some displayables, like images, can't be made bigger or smaller."
    e "这些仅适用于可调整尺寸的组件。图像等组件无法缩放。"

# game/indepth_style.rpy:299
translate zh_cn style_general_cd5cc97c:

    # e "The area property takes a tuple - a parenthesis bounded list of four items. The first two give the position, and the second two the size."
    e "area属性接收元组（括号包裹的四项列表）。前两项为位置，后两项为尺寸。"

# game/indepth_style.rpy:308
translate zh_cn style_general_e5a58f0b:

    # e "Finally, the alt property changes the text used by self-voicing for the hearing impaired."
    e "最后，alt属性改变为听障人士提供的自助语音播报文本。"

# game/indepth_style.rpy:335
translate zh_cn style_text_fe457b8f:

    # e "The text style properties apply to text and input displayables."
    e "文本样式属性适用于文本和输入可视组件。"

# game/indepth_style.rpy:337
translate zh_cn style_text_7ab53f03:

    # e "Text displayables can be created implicitly or explicitly. For example, a textbutton creates a text displayable with a style ending in button_text."
    e "文本可视组件可隐式或显式创建。例如textbutton创建的文本组件使用以button_text结尾的样式。"

# game/indepth_style.rpy:339
translate zh_cn style_text_6dd42a57:

    # e "These can also be set in gui.rpy by changing or defining variables with names like gui.button_text_size."
    e "这些也可在gui.rpy中通过修改或定义类似gui.button_text_size的变量来设置。"

# game/indepth_style.rpy:347
translate zh_cn style_text_c689130e:

    # e "The bold style property makes the text bold. This can be done using an algorithm, rather than a different version of the font."
    e "bold样式属性使文本加粗。可通过算法实现，无需使用字体变体。"

# game/indepth_style.rpy:355
translate zh_cn style_text_3420bfe4:

    # e "The color property changes the color of the text. It takes hex color codes, just like everything else in Ren'Py."
    e "color属性改变文本颜色。采用十六进制色值，与Ren'Py其他设定一致。"

# game/indepth_style.rpy:363
translate zh_cn style_text_14bd6327:

    # e "The first_indent style property determines how far the first line is indented."
    e "first_indent样式属性决定首行缩进距离。"

# game/indepth_style.rpy:371
translate zh_cn style_text_779ac517:

    # e "The font style property changes the font the text uses. Ren'Py takes TrueType and OpenType fonts, and you'll have to include the font file as part of your visual novel."
    e "font属性更改文本字体。Ren'Py支持TrueType和OpenType字体，需将字体文件包含在视觉小说中。"

# game/indepth_style.rpy:379
translate zh_cn style_text_917e2bca:

    # e "The size property changes the size of the text."
    e "size属性改变文本尺寸。"

# game/indepth_style.rpy:388
translate zh_cn style_text_1a46cd43:

    # e "The italic property makes the text italic. Again, this is better done with a font, but for short amounts of text Ren'Py can do it for you."
    e "italic属性使文本倾斜。同样建议使用字体实现，但短文本可由Ren'Py处理。"

# game/indepth_style.rpy:397
translate zh_cn style_text_472f382d:

    # e "The justify property makes the text justified, lining all but the last line up on the left and the right side."
    e "justify属性使文本两端对齐（末行除外）。"

# game/indepth_style.rpy:405
translate zh_cn style_text_87b075f8:

    # e "The kerning property kerns the text. When it's negative, characters are closer together. When positive, characters are farther apart."
    e "kerning属性调整字距。负值使字符更紧密，正值使字符更稀疏。"

# game/indepth_style.rpy:415
translate zh_cn style_text_fe7dec14:

    # e "The line_leading and line_spacing properties put spacing before each line, and between lines, respectively."
    e "line_leading和line_spacing属性分别在每行前和行间添加间距。"

# game/indepth_style.rpy:424
translate zh_cn style_text_aee9277a:

    # e "The outlines property puts outlines around text. This takes a list of tuples, which is a bit complicated."
    e "outlines属性为文本添加描边。接收元组列表，稍显复杂。"

# game/indepth_style.rpy:426
translate zh_cn style_text_b4c5190f:

    # e "But if you ignore the brackets and parenthesis, you have the width of the outline, the color, and then horizontal and vertical offsets."
    e "若忽略括号，参数依次为：描边宽度、颜色、水平偏移量、垂直偏移量。"

# game/indepth_style.rpy:434
translate zh_cn style_text_5a0c2c02:

    # e "The rest_indent property controls the indentation of lines after the first one."
    e "rest_indent属性控制首行后各行的缩进。"

# game/indepth_style.rpy:443
translate zh_cn style_text_430c1959:

    # e "The textalign property controls the positioning of multiple lines of text inside the text displayable. For example, 0.5 means centered." id style_text_430c1959
    e "textalign属性控制多行文本在文本框内的定位。例如0.5表示居中。" id style_text_430c1959

# game/indepth_style.rpy:445
translate zh_cn style_text_19aa0833:

    # e "It doesn't change the position of the text displayable itself. For that, you'll often want to set the textalign and xalign to the same value." id style_text_19aa0833
    e "它不改变文本框本身位置。为此通常需将textalign和xalign设为相同值。" id style_text_19aa0833

# game/indepth_style.rpy:455
translate zh_cn style_text_efc3c392:

    # e "When both textalign and xalign are set to 1.0, the text is properly right-justified." id style_text_efc3c392
    e "当textalign和xalign均为1.0时，文本实现完全右对齐。" id style_text_efc3c392

# game/indepth_style.rpy:464
translate zh_cn style_text_43be63b9:

    # e "The underline property underlines the text."
    e "underline属性为文本添加下划线。"

# game/indepth_style.rpy:471
translate zh_cn style_text_343f6d34:

    # e "Those are the most common text style properties, but not the only ones. Here are a few more that you might need in special circumstances."
    e "以上是常用文本样式属性，但非全部。以下是特殊场景可能需要的属性："

# game/indepth_style.rpy:479
translate zh_cn style_text_e7204a95:

    # e "By default, text in Ren'Py is antialiased, to smooth the edges. The antialias property can turn that off, and make the text a little more jagged."
    e "Ren'Py文本默认抗锯齿平滑边缘。antialias属性可关闭该功能，使文本略显锯齿。"

# game/indepth_style.rpy:487
translate zh_cn style_text_a5316e4c:

    # e "The adjust_spacing property is a very subtle one, that only matters when a player resizes the window. When True, characters will be shifted a bit so the Text has the same relative spacing."
    e "adjust_spacing是极细微的属性，仅在玩家调整窗口大小时生效。设为True时，字符会微调以保持相对间距。"

# game/indepth_style.rpy:496
translate zh_cn style_text_605d4e4a:

    # e "When False, the text won't jump around as much. But it can be a little wider or narrower based on screen size."
    e "设为False则文本跳动较少，但宽度可能随屏幕尺寸变化。"

# game/indepth_style.rpy:505
translate zh_cn style_text_acf8a0e1:

    # e "The layout property has a few special values that control where lines are broken. The 'nobreak' value disables line breaks entirely, making the text wider."
    e "layout属性有特殊值控制断行。'nobreak'值禁用换行，使文本更宽。"

# game/indepth_style.rpy:516
translate zh_cn style_text_785729cf:

    # e "When the layout property is set to 'subtitle', the line breaking algorithm is changed to try to make all lines even in length, as subtitles usually are."
    e "设为'subtitle'时，断行算法会尝试使各行长度均等（如字幕效果）。"

# game/indepth_style.rpy:524
translate zh_cn style_text_9c26f218:

    # e "The strikethrough property draws a line through the text. It seems pretty unlikely you'd want to use this one."
    e "strikethrough属性为文本添加删除线。使用场景可能较少。"

# game/indepth_style.rpy:534
translate zh_cn style_text_c7229243:

    # e "The vertical style property places text in a vertical layout. It's meant for Asian languages with special fonts."
    e "vertical属性实现文本竖排布局，适用于特殊字体的亚洲语言。"

# game/indepth_style.rpy:540
translate zh_cn style_text_724bd5e0:

    # e "And those are the text style properties. There might be a lot of them, but we want to give you a lot of control over how you present text to your players."
    e "以上是文本样式属性。虽然数量众多，但我们希望赋予你对文本呈现方式的充分控制权。"

# game/indepth_style.rpy:580
translate zh_cn style_button_300b6af5:

    # e "Next up, we have the window and button style properties. These apply to windows like the text window at the bottom of this screen and frames like the ones we show examples in."
    e "接下来是窗口和按钮样式属性。适用于本屏底部的文本框等窗口，以及示例中的框架。"

# game/indepth_style.rpy:582
translate zh_cn style_button_255a18e4:

    # e "These properties also apply to buttons, in-game and out-of-game. To Ren'Py, a button is a window you can click."
    e "这些属性也适用于游戏内外按钮。对Ren'Py而言，按钮是可点击的窗口。"

# game/indepth_style.rpy:593
translate zh_cn style_button_9b53ce93:

    # e "I'll start off with this style, which everything will inherit from. To make our lives easier, it inherits from the default style, rather than the customized buttons in this game's GUI." id style_button_9b53ce93
    e "我将从这个所有元素继承的样式开始演示。为简化操作，它继承自默认样式而非本游戏GUI的自定义按钮。" id style_button_9b53ce93

# game/indepth_style.rpy:595
translate zh_cn style_button_aece4a8c:

    # e "The first style property is the background property. It adds a background to a button or window. Since this is a button, idle and hover variants choose different backgrounds when focused." id style_button_aece4a8c
    e "首个样式属性是background。为按钮/窗口添加背景。作为按钮，idle和hover变体在聚焦时选用不同背景。" id style_button_aece4a8c

# game/indepth_style.rpy:597
translate zh_cn style_button_b969f04a:

    # e "We also center the two buttons, using the xalign position property."
    e "我们还使用xalign位置属性使双按钮居中。"

# game/indepth_style.rpy:601
translate zh_cn style_button_269ae069:

    # e "We've also customized the style of the button's text, using this style. It centers the text and makes it change color when hovered."
    e "通过此样式自定义了按钮文本：文本居中且在悬停时变色。"

# game/indepth_style.rpy:612
translate zh_cn style_button_1009f3e1:

    # e "Without any padding around the text, the button looks odd. Ren'Py has padding properties that add space inside the button's background."
    e "文本无内边距时按钮显示异常。Ren'Py的padding属性可在背景内添加间距。"

# game/indepth_style.rpy:621
translate zh_cn style_button_5bdfa45a:

    # e "More commonly used are the xpadding and ypadding style properties, which add the same padding to the left and right, or the top and bottom, respectively."
    e "更常用的是xpadding和ypadding，分别添加左右/上下对称内边距。"

# game/indepth_style.rpy:629
translate zh_cn style_button_81283d42:

    # e "The margin style properties work the same way, except they add space outside the background. The full set exists: left_margin, right_margin, top_margin, bottom_margin, xmargin, and ymargin."
    e "margin属性原理相同，但在背景外添加间距。完整属性包括：left_margin, right_margin, top_margin, bottom_margin, xmargin, ymargin。"

# game/indepth_style.rpy:638
translate zh_cn style_button_0b7aca6b:

    # e "The size_group style property takes a string. Ren'Py will make sure that all the windows or buttons with the same size_group string are the same size."
    e "size_group属性接收字符串。Ren'Py将确保同组字符串的窗口/按钮尺寸一致。"

# game/indepth_style.rpy:647
translate zh_cn style_button_4c6da7d9:

    # e "Alternatively, the xfill and yfill style properties make a button take up all available space in the horizontal or vertical directions."
    e "或者，xfill和yfill属性使按钮占满水平/垂直可用空间。"

# game/indepth_style.rpy:657
translate zh_cn style_button_fd5338b2:

    # e "The foreground property gives a displayable that is placed on top of the contents and background of the window or button."
    e "foreground属性提供覆盖窗口/按钮内容和背景的可视组件。"

# game/indepth_style.rpy:659
translate zh_cn style_button_b8af697c:

    # e "One way to use it is to provide extra decorations to a button that's serving as a checkbox. Another would be to use it with a Frame to provide a glossy shine that overlays the button's contents."
    e "可用作复选框按钮的额外装饰，或配合Frame为按钮内容添加光泽覆盖层。"

# game/indepth_style.rpy:668
translate zh_cn style_button_c0b1b62e:

    # e "There are also a few style properties that only apply to buttons. The hover_sound and activate_sound properties play sound files when a button is focused and activated, respectively."
    e "部分样式属性仅适用于按钮：hover_sound和activate_sound分别在按钮聚焦和激活时播放音效。"

# game/indepth_style.rpy:677
translate zh_cn style_button_02fa647e:

    # e "Finally, the focus_mask property applies to partially transparent buttons. When it's set to True, only areas of the button that aren't transparent cause a button to focus."
    e "最后，focus_mask属性应用于半透明按钮。设为True时，仅非透明区域可触发按钮聚焦。"

# game/indepth_style.rpy:757
translate zh_cn style_bar_414d454a:

    # e "To demonstrate styles, let me first show two of the images we'll be using. This is the image we're using for parts of the bar that are empty."
    e "为演示样式，先展示将使用的两幅图像。这是进度条空白部分的图像。"

# game/indepth_style.rpy:761
translate zh_cn style_bar_9422b7b0:

    # e "And here's what we use for parts of the bar that are full."
    e "而这是填充部分的图像。"

# game/indepth_style.rpy:773
translate zh_cn style_bar_8ae6a14b:

    # e "The left_bar and right_bar style properties, and their hover variants, give displayables for the left and right side of the bar. By default, the value is shown on the left."
    e "left_bar和right_bar样式属性（及其hover变体）设定进度条左右侧的显示组件。默认值显示在左侧。"

# game/indepth_style.rpy:775
translate zh_cn style_bar_7f0f50e5:

    # e "Also by default, both the left and right displayables are rendered at the full width of the bar, and then cropped to the appropriate size."
    e "同样默认左右组件按进度条全宽渲染后裁剪至合适尺寸。"

# game/indepth_style.rpy:777
translate zh_cn style_bar_9ef4f62f:

    # e "We give the bar the ysize property to set how tall it is. We could also give it xsize to choose how wide, but here it's limited by the width of the frame it's in."
    e "通过ysize属性设置进度条高度。也可用xsize设置宽度，但此处受所在框架宽度限制。"

# game/indepth_style.rpy:790
translate zh_cn style_bar_d4c29710:

    # e "When the bar_invert style property is True, the bar value is displayed on the right side of the bar. The left_bar and right_bar displayables might also need to be swapped."
    e "当bar_invert属性为True时，进度值显示在右侧。此时可能需要交换left_bar和right_bar组件。"

# game/indepth_style.rpy:804
translate zh_cn style_bar_cca67222:

    # e "The bar_resizing style property causes the bar images to be resized to represent the value, rather than being rendered at full size and cropped."
    e "bar_resizing属性使进度条图像按值缩放，而非全尺寸渲染后裁剪。"

# game/indepth_style.rpy:817
translate zh_cn style_bar_7d361bac:

    # e "The thumb style property gives a thumb image, that's placed based on the bar's value. In the case of a scrollbar, it's resized if possible." id style_bar_7d361bac
    e "thumb属性提供随进度值定位的滑块图像。滚动条中会尽可能调整尺寸。" id style_bar_7d361bac

# game/indepth_style.rpy:819
translate zh_cn style_bar_b6dfb61b:

    # e "Here, we use it with the base_bar style property, which sets both bar images to the same displayable."
    e "此处我们将其与base_bar属性联用，后者将左右图像设为相同组件。"

# game/indepth_style.rpy:834
translate zh_cn style_bar_996466ad:

    # e "The left_gutter and right_gutter properties set a gutter on the left or right size of the bar. The gutter is space the bar can't be dragged into, that can be used for borders."
    e "left_gutter和right_gutter属性设置进度条左右侧间隔区。该区域不可拖动，用于边框装饰。"

# game/indepth_style.rpy:849
translate zh_cn style_bar_fa41a83c:

    # e "The bar_vertical style property displays a vertically oriented bar. All of the other properties change names - left_bar becomes top_bar, while right_bar becomes bottom_bar."
    e "bar_vertical属性实现垂直进度条。所有相关属性名称变更：left_bar变为top_bar，right_bar变为bottom_bar。"

# game/indepth_style.rpy:854
translate zh_cn style_bar_5d33c5dc:

    # e "Finally, there's one style we can't show here, and it's unscrollable. It controls what happens when a scrollbar can't be moved at all."
    e "最后是无法在此演示的unscrollable属性，控制滚动条完全无法移动时的表现。"

# game/indepth_style.rpy:856
translate zh_cn style_bar_e8e32280:

    # e "By default, it's shown. But if unscrollable is 'insensitive', the bar becomes insensitive. If it's 'hide', the bar is hidden, but still takes up space."
    e "默认显示滚动条。若设为'insensitive'则禁用，设为'hide'则隐藏（仍占位）。"

# game/indepth_style.rpy:860
translate zh_cn style_bar_f1292000:

    # e "That's it for the bar properties. By using them, a creator can customize bars, scrollbars, and sliders."
    e "进度条属性讲解完毕。通过它们可自定义进度条、滚动条和滑块。"

# game/indepth_style.rpy:959
translate zh_cn style_box_5fd535f4:

    # e "The hbox displayable is used to lay its children out horizontally. By default, there's no spacing between children, so they run together."
    e "hbox可视组件将其子项水平排列。默认子项间无间距，故紧密相连。"

# game/indepth_style.rpy:965
translate zh_cn style_box_0111e5dc:

    # e "Similarly, the vbox displayable is used to lay its children out vertically. Both support style properties that control placement."
    e "类似地，vbox组件垂直排列子项。两者都支持控制排版的样式属性。"

# game/indepth_style.rpy:970
translate zh_cn style_box_5a44717b:

    # e "To make the size of the box displayable obvious, I'll add a highlight to the box itself, and not the frame containing it."
    e "为使框体尺寸更明显，我将为框体本身（而非其容器框架）添加高亮。"

# game/indepth_style.rpy:978
translate zh_cn style_box_239e7a8f:

    # e "Boxes support the xfill and yfill style properties. These properties make a box expand to fill the available space, rather than the space of the largest child."
    e "框体支持xfill和yfill属性。这些属性使框体扩展至可用空间，而非仅适应最大子项。"

# game/indepth_style.rpy:988
translate zh_cn style_box_e513c946:

    # e "The spacing style property takes a value in pixels, and adds that much spacing between each child of the box."
    e "spacing属性接收像素值，在框体各子项间添加间距。"

# game/indepth_style.rpy:998
translate zh_cn style_box_6ae4f94d:

    # e "The first_spacing style property is similar, but it only adds space between the first and second children. This is useful when the first child is a title that needs different spacing."
    e "first_spacing属性类似，但仅在首个子项后添加间距。适用于首项为需特殊间距的标题时。"

# game/indepth_style.rpy:1008
translate zh_cn style_box_0c518d9f:

    # e "The box_reverse style property reverses the order of entries in the box."
    e "box_reverse属性反转框体内条目顺序。"

# game/indepth_style.rpy:1021
translate zh_cn style_box_f73c1422:

    # e "We'll switch back to a horizontal box for our next example."
    e "下个示例将切换回水平框体。"

# game/indepth_style.rpy:1031
translate zh_cn style_box_285592bb:

    # e "The box_wrap style property fills the box with children until it's full, then starts again on the next line."
    e "box_wrap属性使框体填满子项后自动换行。"

# game/indepth_style.rpy:1044
translate zh_cn style_box_a7637552:

    # e "Grids bring with them two more style properties. The xspacing and yspacing properties control spacing in the horizontal and vertical directions, respectively."
    e "网格布局另有两个样式属性：xspacing和yspacing分别控制水平/垂直间距。"

# game/indepth_style.rpy:1051
translate zh_cn style_box_4006f74b:

    # e "Lastly, we have the fixed layout. The fixed layout usually expands to fill all space, and shows its children from back to front."
    e "最后是固定布局(fixed)。固定布局通常扩展占满空间，并按从后往前顺序显示子项。"

# game/indepth_style.rpy:1053
translate zh_cn style_box_4a2866f0:

    # e "But of course, we have some style properties that can change that."
    e "当然也有样式属性可改变此行为。"

# game/indepth_style.rpy:1062
translate zh_cn style_box_66e042c4:

    # e "When the xfit style property is True, the fixed lays out all its children as if it was full size, and then shrinks in width to fit them. The yfit style works the same way, but in height."
    e "当xfit属性为True时，固定布局先按全尺寸排布子项，再收缩宽度适应。yfit属性同理控制高度。"

# game/indepth_style.rpy:1070
translate zh_cn style_box_6a593b10:

    # e "The order_reverse style property changes the order in which the children are shown. Instead of back-to-front, they're displayed front-to-back."
    e "order_reverse属性改变子项显示顺序：从前往后而非从后往前。"

# game/indepth_style.rpy:1082
translate zh_cn style_inspector_21bc0709:

    # e "Sometimes it's hard to figure out what style is being used for a particular displayable. The displayable inspector can help with that."
    e "有时难以确定特定可视组件使用的样式。显示组件检查器可解决此问题。"

# game/indepth_style.rpy:1084
translate zh_cn style_inspector_243c50f0:

    # e "To use it, place the mouse over a portion of the Ren'Py user interface, and hit shift+I. That's I for inspector."
    e "使用方式：将鼠标悬停在Ren'Py用户界面上，按shift+I（I代表检查器inspect）。"

# game/indepth_style.rpy:1086
translate zh_cn style_inspector_bcbdc396:

    # e "Ren'Py will pop up a list of displayables the mouse is over. Next to each is the name of the style that displayable uses."
    e "Ren'Py将弹出鼠标悬停处的可视组件列表。每项旁标注其使用的样式名称。"

# game/indepth_style.rpy:1088
translate zh_cn style_inspector_d981e5c8:

    # e "You can click on the name of the style to see where it gets its properties from."
    e "点击样式名可查看属性来源。"

# game/indepth_style.rpy:1090
translate zh_cn style_inspector_ef46b86d:

    # e "By default, the inspector only shows interface elements like screens, and not images. Type shift+alt+I if you'd like to see images as well."
    e "默认检查器仅显示界面元素（如界面），不显示图像。按shift+alt+I可同时查看图像。"

# game/indepth_style.rpy:1092
translate zh_cn style_inspector_b59c6b69:

    # e "You can try the inspector right now, by hovering this text and hitting shift+I."
    e "你可立即尝试：悬停本段文字并按shift+I。"

translate zh_cn strings:

    # game/indepth_style.rpy:20
    old "Button 1"
    new "按钮一"

    # game/indepth_style.rpy:22
    old "Button 2"
    new "按钮二"

    # game/indepth_style.rpy:66
    old "Style basics."
    new "样式基础"

    # game/indepth_style.rpy:66
    old "General style properties."
    new "通用样式属性"

    # game/indepth_style.rpy:66
    old "Text style properties."
    new "文本样式属性"

    # game/indepth_style.rpy:66
    old "Window and Button style properties."
    new "窗口与按钮样式属性"

    # game/indepth_style.rpy:66
    old "Bar style properties."
    new "进度条样式属性"

    # game/indepth_style.rpy:66
    old "Box, Grid, and Fixed style properties."
    new "框体、网格与固定布局样式属性"

    # game/indepth_style.rpy:66
    old "The Displayable Inspector."
    new "可视组件检查器"

    # game/indepth_style.rpy:66
    old "That's all I want to know."
    new "我已了解全部内容"

    # game/indepth_style.rpy:112
    old "This text is colored green."
    new "此文本为绿色"

    # game/indepth_style.rpy:126
    old "Danger"
    new "危险"

    # game/indepth_style.rpy:142
    old "This text is colored red."
    new "此文本为红色"

    # game/indepth_style.rpy:170
    old "This text is colored blue."
    new "此文本为蓝色"

    # game/indepth_style.rpy:248
    old "Orbiting Earth in the spaceship, I saw how beautiful our planet is.\n–Yuri Gagarin"
    new "在宇宙飞船中环游地球时，我惊叹于家园的美丽。\n——尤里·加加林"

    # game/indepth_style.rpy:303
    old "\"Orbiting Earth in the spaceship, I saw how beautiful our planet is.\" Said by Yuri Gagarin."
    new "\"在宇宙飞船中环游地球时，我惊叹于家园的美丽。\" 尤里·加加林所言。"

    # game/indepth_style.rpy:326
    old "Vertical"
    new "垂直排列"

    # game/indepth_style.rpy:329
    old "Far better it is to dare mighty things, to win glorious triumphs, even though checkered by failure, than to rank with those poor spirits who neither enjoy nor suffer much, because they live in the gray twilight that knows not victory nor defeat.\n\n–Theodore Roosevelt"
    new "敢于挑战伟业，赢取辉煌胜利，纵使经历失败，也远胜于那些在灰色黄昏中徘徊的灵魂——他们既不懂欢欣亦不解苦痛，因其生命游离于胜负之外。\n\n——西奥多·罗斯福"

    # game/indepth_style.rpy:561
    old "Top Choice"
    new "顶部选项"

    # game/indepth_style.rpy:566
    old "Bottom Choice"
    new "底部选项"

    # game/indepth_style.rpy:877
    old "First Child"
    new "首个子项"

    # game/indepth_style.rpy:878
    old "Second Child"
    new "第二个子项"

    # game/indepth_style.rpy:879
    old "Third Child"
    new "第三个子项"

    # game/indepth_style.rpy:882
    old "Fourth Child"
    new "第四个子项"

    # game/indepth_style.rpy:883
    old "Fifth Child"
    new "第五个子项"

    # game/indepth_style.rpy:884
    old "Sixth Child"
    new "第六个子项"

