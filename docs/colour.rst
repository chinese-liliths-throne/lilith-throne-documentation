.. include:: global.inc.rst
=============
颜色
=============

    :Authors: innoxia, Mr.Lee, CK_Rainbow

颜色(Colours)在游戏中多处可以使用。

你可以在 :ltgithub:`res/colours/` 文件夹中找到正在使用的颜色。

通用信息
-----------

在xml文件中，根元素的标签需要设置为 ``colour``。

metallic
------------

该元素是 :ref:`optional`，决定了这种颜色是否拥有金属质感。若是，游戏会为该颜色的图标生成金属效果。

左图为 ``true`` 的效果，右图为 ``false`` 的效果:

.. image:: /img/colour/metallicTrue.png
.. image:: /img/colour/metallicFalse.png

name
--------

该颜色的名称，会显示在游戏的悬浮提示栏中。

.. code:: xml

    <name><![CDATA[黑夜般的深黑色]]></name>

colour
---------

深色主题时显示的颜色。


lightColour
--------------

浅色主题时显示的颜色，一般情况下应和上述属性相同， **但如果在亮色主题中表现不理想，应适当微调**。

coveringIconColour
---------------------

该元素是 :ref:`optional`，定义了在转化界面中显示颜色图标时用的颜色，若留空将会使用 ``colour`` 属性的颜色。

formattingNames
--------------------------

该元素是 :ref:`optional`，定义了一般用于 :ref:`parse` 的别名，并不会直接在游戏中显示，每个定义的别名(例如:Colour)都将在游戏中以 ``Colour``、 ``italicColour``、 ``blodColour``、 ``glowColour`` 四种形式出现。(建议使用首字母大写的英文单词)

若未定义，则无法在解析时使用该颜色。

每一种别名都将在该元素内以 `format-name`_ 标签的形式出现。可以定义多个 ``name`` 标签。

.. _format-name:

name
~~~~~~~~~

定义了这个颜色的一个别名。

.. code:: xml

	<formattingNames>
		<name><![CDATA[别名1]]></name>
		<name><![CDATA[别名2]]></name>
	</formattingNames>

tags
--------

该元素是 :ref:`optional`，决定了这个颜色属于何种类型(是否可泛用于皮毛、眼睛、皮肤等部位的颜色选择)。
每一种类型都将在该元素内以 `tag`_ 标签的形式出现。可以定义多个 ``tag`` 标签。

tag
~~~~~~~~

定义了这个颜色所属的一种类型。其中可填入的内容请参见 :ref:`constant-colour-tag`。(或源码 :ltgithub:`src/com/lilithsthrone/utils/colours/ColourTag.java`)

.. code:: xml

	<tags>
		<tag>SKIN</tag>
		<tag>SLIME_NATURAL</tag>
	</tags>

