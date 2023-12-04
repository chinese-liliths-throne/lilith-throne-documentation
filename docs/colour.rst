.. include:: global.inc.rst
=============
colour文件夹
=============

    :Authors: innoxia, Mr.Lee

此页主要由Mr.Lee编写,本人代指Mr.Lee
本人能力有限,对莉莉丝还处于探索阶段,可能存在错误,请谅解

本页是基于innoxia的mod模板( :ltgithub:`res/mods/innoxia/colours/fuchsia.xml` )写的
本页中的 ``Color`` 为 ``javafx.scene.paint.Color``

通用信息
---------

在xml文件中，根元素的标签需要设置为 ``colour``。

在这里mod可以自定义颜色,得到一个Colour(源码: :ltgithub:`src/com/lilithsthrone/utils/colours/Colour.java` )实例

metallic
---------

这是不是金属色?
如果是金属色,游戏会为该颜色的图标生成金属效果

左图为true的效果,右图为false的效果:

.. image:: \\img\\colour\\metallicTrue.png
.. image:: \\img\\colour\\metallicFalse.png
对应的 ``Colour`` 类的 ``boolean metallic`` 属性

name
------

这个颜色的名称,会被显示到游戏的提示工具里

.. code:: xml

    <name><![CDATA[黑夜般的深黑色]]></name>

效果

.. image:: \\img\\colour\\name.png

对应 ``Colour`` 类的 ``String name`` 属性

colour
-------

深色主题时显示的颜色

对应 ``Colour`` 类的 ``Color colour`` 属性

lightColour
------------

浅色主题是显示的颜色,一般情况下应和上述属性相同,但如果在亮色主题中表现不理想,应适当微调

对应 ``Colour`` 类的 ``Color lightColour`` 属性

coveringIconColour
---------------------

在变形界面里显示颜色的图标时用的颜色,留空的话将会使用 ``colour`` 属性的颜色

对应lightColour属性对应 ``Colour`` 类的 ``Color coveringIconColour`` 属性

formattingNames
-----------------

定义能在内置解释器识别为指令的别名,解释器内部会衍生出四个上色指令
填写的内容应被 ``<name>`` 标签修饰
必须要写,不能省略省略

示例:

.. code:: xml

	<formattingNames>
		<name><![CDATA[别名1]]></name>
		<name><![CDATA[别名2]]></name>
	</formattingNames>

结果:

.. image:: \\img\\colour\\formattingNames.png

对应 ``Colour`` 类的 ``List<String> formattingNames`` 属性


tags
~~~~~

决定这是那种类型的覆盖颜色(是否可泛用于皮毛、眼睛、皮肤……等部位的颜色选择)
填写的内容应被 ``<tag>`` 标签修饰
这个页可以省略不写

例:

.. code:: xml

	<tags>
		<tag>SKIN</tag>
		<tag>SLIME_NATURAL</tag>
	</tags>


\ `附表1 tag含义(总结日期:23.11.26)`_\

对应 ``Colour`` 类的 ``List<ColourTag> tags`` 属性

附表
-----

附表1 tag含义(总结日期:23.11.26)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**自然(_NATURAL)表示可以刷怪刷出来,*非自然(_DYE)* 表示只能通过转化获得**

源码 :ltgithub:`src/com/lilithsthrone/utils/colours/ColourTag.java`

(部分翻译的不太确定,请后人来更正吧)

======================	=====
SKIN					皮肤
SLIME_NATURAL			*自然* 黏液
SLIME_DYE				*非自然* 黏液
FEATHER_NATURAL			*自然* 羽毛
FEATHER_DYE				*非自然* 染色
FUR						福瑞
SCALE					巩膜
HORN
ANTLER					
HAIR					头发
GENERIC_COVERING		此标签将把颜色添加到"所有覆盖物"列表中
MAKEUP					可以用作化妆染料
IRIS_NATURAL			*自然* 产生的虹膜颜色,可用于非捕食性(non-predatory)种族
IRIS_DYE				*非自然* 产生的虹膜颜色,可用于非捕食性(non-predatory)种族
IRIS_PREDATOR_NATURAL	*自然* 产生的虹膜颜色,可用于捕食性(predatory)种族
IRIS_PREDATOR_DYE		*非自然* 产生的虹膜颜色,可用于捕食性(predatory)种族
PUPIL_NATURAL			*自然* 产生的瞳孔颜色
PUPIL_DYE				*非自然* 产生的瞳孔颜色
SCLERA_NATURAL			*自然* 产生的眼白颜色
SCLERA_DYE				*非自然* 产生的眼白颜色
======================	=====

附表2 Colour类粗分析
~~~~~~~~~~~~~~~~~~~

public方法:

======================================================================	====
boolean isMod															返回 ``boolean mod`` 属性,个人感觉是用来判断这是否是来自mod的颜色
boolean isFromExternalFile												返回 ``boolean fromExternalFile`` 属性,个人感觉是用来判断这是否是从xml加载的颜色
String toRGBA															返回 ``String rbga(r,g,b,a)`` r,g,b范围均为0-255(个人感觉a也是)
String toWebHexString													返回自身的16进制颜色代码,ex: #RRGGBB
String getCoveringIconColour											返回 ``boolean coveringIconColour`` 属性的16进制颜色代码,ex: #RRGGBB
Color getColor															若当前是亮色主题,返回 ``Color lightColour`` 属性,否则返回 ``Color colour`` 属性
boolean isMetallic														返回 ``boolean metallic`` 属性
boolean isRainbow														返回是否是彩虹颜色
List<String> getRainbowColours											非彩虹颜色返回 ``null`` ,彩色颜色涉及方法重写
String getRainbowDiv(int rainbowPixels)									非彩虹颜色返回 ``""`` (彩虹颜色看的不太懂)
String getName															返回 ``String name`` 属性
String getId															返回自身ID
String toString															不应该对 ``Colour`` 使用该方法,将用 *getId* 替代
Colour setLinkedColourDarker(Colour)									将自身的 ``colourLinkDarker`` 属性设为指定的 ``Colour`` ,指定的 ``Colour`` 的 ``colourLinkLighter`` 属性设为自身,返回自身
Colour getLinkedColourDarker											返回 ``colourLinkDarker`` 属性
List<Colour> getDarkerLinkedColours										返回一个颜色逐渐加深的列表,最亮的颜色索引为0,返回值可能是空列表
Colour setLinkedColourLighter(Colour)									将自身的 ``colourLinkLighter`` 属性设为指定的 ``Colour`` ,指定的 ``Colour`` 的 ``colourLinkDarker`` 属性设为自身,返回自身
Colour getLinkedColourLighter											返回 ``colourLinkLighter`` 属性
List<Colour> getLighterLinkedColours									返回一个颜色逐渐变亮的列表,最深的颜色索引为0,返回值可能是空列表
String[] getShades(int shadesCount, boolean rgba, float opacity)		所有参数或者第二第三参数可以省略不填,第一个参数不用填时默认为5,剩下的目前不会
String[] getShadesRgbaFormat											不会
List<String> getFormattingNames											返回 ``List<ColourTag> tags`` 属性,若该属性为 ``null`` 返回空列表
boolean isOneOf															判断自身是否在某一颜色列表中
======================================================================	====

附表3 Colour汉化过模板
~~~~~~~~~~~~~~~~~~~~~

.. code:: xml

	<?xml version='1.0' encoding='UTF-8' standalone='no'?>
	<colour>
		<!-- GENERAL INFORMATION: If you are unsure of anything, please use the LT Discord to ask for help! -->
		
		<!-- 这是不是金属色?
		如果是金属色,游戏会为该颜色的图标生成金属效果 -->
		<metallic>false</metallic>
		
		<!-- 名字. -->
		<name><![CDATA[深黑色]]></name>
		
		<!-- 深色主题时显示的颜色 -->
		<colour>747474</colour>
		<!-- 浅色主题时显示的颜色
		在用于物品或种族上色的情况下,和上面相同即可 -->
		<lightColour>747474</lightColour>
		<!-- 在变形界面对颜色标注时展示的颜色,应该和上面俩相同
		你可以省略不写,那么值就是<colour>值 -->
		<coveringIconColour>747474</coveringIconColour>
		
		<!-- 定义后可以这样些[style.colour名字1(文本)][style.colour名字2(文本)]等指令使用
		这个东西会污染内置的指令说明(里面其实被污染的差不多了……1000+都是这种生成的指令)
		经测试这东西不写还会导致内置的指令/指令列表不能使用…… -->
		<formattingNames>
			<name><![CDATA[别名]]></name>
			<name><![CDATA[别名]]></name>
		</formattingNames>
		
		<!-- 
		决定该颜色是否添加到游戏的覆盖颜色(用于皮毛、眼睛、皮肤……)
		(23.11.26)
		自然表示可以刷出来,非自然表示只能通过转化获得
		SKIN					皮肤
		SLIME_NATURAL			自然黏液
		SLIME_DYE				非自然黏液
		FEATHER_NATURAL			自然羽毛
		FEATHER_DYE				非自然染色
		FUR						福瑞
		SCALE					巩膜
		HORN
		ANTLER					
		HAIR					头发
		GENERIC_COVERING		此标签将把颜色添加到“所有覆盖物”列表中：
		MAKEUP					可以用作化妆染料
		IRIS_NATURAL			自然产生的虹膜颜色,可用于非捕食性(non-predatory)种族
		IRIS_DYE				非自然产生的虹膜颜色,可用于非捕食性(non-predatory)种族
		IRIS_PREDATOR_NATURAL	自然产生的虹膜颜色,可用于捕食性(predatory)种族
		IRIS_PREDATOR_DYE		非自然产生的虹膜颜色,可用于捕食性(predatory)种族
		PUPIL_NATURAL			自然产生的瞳孔颜色
		PUPIL_DYE				非自然产生的虹膜颜色
		SCLERA_NATURAL			自然产生的眼白颜色
		SCLERA_DYE				非自然产生的眼白颜色
		可以在这里查询: https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/utils/colours/ColourTag.java -->
		<tags>
			<tag>SKIN</tag>
		</tags>
		
	</colour>
