.. include:: global.inc.rst

.. _place_types:

============
地点类型
============

    :Authors: innoxia, CK_Rainbow, AceXP

地点类型(Place types)是与世界类型绑定的一种数据，在游戏中的直观表现便是每一个不同的地图格。

你可以在 :ltgithub:`res/maps/authorName/customId/placeTypes` 文件夹中找到正在使用的偶遇事件。

通用信息
--------------

在xml文件中，根元素的标签需要设置为 ``placeType``。

worldRegion
---------------------------

该元素代表了该地点类型所处的世界区域，而世界区域则影响着不同种族的生成概率，可填入的内容请参见 :ltgithub:`src/com/lilithsthrone/world/WorldRegion.java`。下面的例子中代表该地点类型属于 ``DOMINION``。

.. code:: xml

    <worldRegion>DOMINION</worldRegion>

name
--------------

该元素定义了该地点类型的名称。该名称会用于UI显示。

tooltipDescription
-----------------------------

该元素定义了该地点类型的描述。该描述会在鼠标悬浮至该类型的地图格上时出现的悬浮提示栏中显示。

virginityLossDescription
-----------------------------

该元素中定义了若在该地点类型中发生了处女膜破裂事件，会在角色总览界面显示的部分描述。下面的例子在游戏中即表现为“失去了xxx于莉莱雅的地牢中”。

.. code:: xml

	<virginityLossDescription><![CDATA[in Lilaya's dungeon]]></virginityLossDescription>

sexBlockedReason
-----------------------------

该元素定义了是否能够在该地点类型进行性爱，若不行，那么将会显示什么内容。该元素是 :ref:`optional`，如果该元素留空，内容的返回值为空或制表符，那么代表着在该地点类型能够进行性爱。

sexBlockedFromCharacterPresent
--------------------------------

该元素决定了如果该位置有 **非奴隶、非元素、非同伴** 的角色存在，是否会导致无法在此处进行性爱。该元素的数值为 :ref:`boolean-values`。

.. index:: base-colour

colour
---------------------

该元素定义了该地点类型的颜色，决定了地点标题的颜色、地图格上图案、边框的颜色等。有关填入内容的具体情况请参见 :ref:`colours`。

backgroundColour
---------------------

该元素定义了该地点类型的背景颜色，决定了地图格的底色。与 `colour`_ 基本相似，一般都使用 ``MAP_BACKGROUND``。

encounterType
-----------------

该元素定义了该地点类型的 `偶遇事件 <encounters.html>`_ ，可以为该地点类型添加一个固有的偶遇事件，是一个 :ref:`optional`，可填入的内容请参见 :ref:`items-identifier`，同时若填入 ``null`` 也将视为无效，如下方的例子所示。

.. code:: xml

	<encounterType>null</encounterType>

dialogue
-------------

该元素定义了该地点类型的默认对话节点，每当行进到该地点类型时，将会自动触发该对话节点。


populationPresent
-------------------

该元素定义了该地点类型会出现的人群类型。该元素是 :ref:`optional`，若留空，则代表该地点类型不会出现任何人群。每一种人群都将在该元素内以 `population`_ 标签的形式出现。可以定义多个 ``population`` 标签。

**节点属性:**
    .. nodevar:: [copyPlaceType] <constant> ()

        属性 ``copyPlaceType`` 的数值应填写一个地点类型的标识符，详见 :ref:`items-identifier`，该属性的作用是将对应地点类型的人群类型复制到当前地点类型中。若填写该值，则可以省略 ``populationPresent`` 元素内的 ``population`` 元素。

population
---------------------

该元素定义了特定的一种人群类型，其属性以及内部的元素定义了该类人群的具体情况。

**节点属性:**
    .. nodevar:: [night] <boolean> ()

	.. nodevar:: [day] <boolean> ()

        属性 ``night`` 和 ``day`` 的数值应填写布尔值，分别代表该类人群在夜晚时段和白天时段出现。请注意此处的设置会覆盖下方的属性！建议只使用这两个属性其中之一，或使用下方的三个属性。

	.. nodevar:: [startMinutes] <int> ()

	.. nodevar:: [endMinutes] <int> ()

	.. nodevar:: [inclusiveRange] <boolean> (true)

		属性 ``startMinutes`` 和 ``endMinutes`` 的数值应填写一个整数，代表了该人群的出现时间段，单位为分钟。若留空，则代表仅限白天时段。
		
		属性 ``inclusiveRange`` 为 ``true`` 代表从 ``startMinutes`` 到 ``endMinutes`` 为，而 ``false`` 代表从 ``endMinutes`` 到次日 ``startMinutes``。

		若均未定义，则代表该类人群永远都会出现。

conditional
~~~~~~~~~~~~~~~

该元素可以额外决定该类人群的出现条件，是 :ref:`optional`。该元素的内容会被 :ref:`parse` ，返回值应为 :ref:`boolean-values`。理论上非 ``true`` 的返回值都会视作 ``false``。


populationType
~~~~~~~~~~~~~~~~~~

该元素定义了该类人群的类型，可填入的内容请参见 :ltgithub:`src/com/lilithsthrone/world/population/PopulationType.java`。此外还可以填入不属于文件中的内容，而填入其中的文本将会被 **直接当作人群的名称显示**。

**节点属性:**
    .. nodevar:: [plural] <boolean> (false)

		属性 ``plural`` 的数值应填写布尔值，代表该类人群的名称是否为复数形式。若留空，则默认为单数形式。

	.. nodevar:: density <constant> ()

		属性 ``density`` 决定了该人群的密度，可填入的内容请参见 :ltgithub:`src/com/lilithsthrone/world/population/PopulationDensity.java`。

subspeciesPresent
~~~~~~~~~~~~~~~~~~~

该元素定义了该类人群中会出现的亚种类型。每一种亚种都将在该元素内以 `subspecies`_ 标签的形式出现。可以定义多个 ``subspecies`` 标签。

**节点属性:**
	.. nodevar:: [worldType] <constant> ()

		属性 ``worldType`` 决定了出现的亚种类型取自哪个世界类型，应填写一个世界类型的标识符，详见 :ref:`items-identifier`。若填写该值，则可以省略 ``subspeciesPresent`` 元素内的 ``subspecies`` 元素，但同时可以填入 `subspeciesToRemove`_，以去除某些亚种。若留空，则完全通过定义的 ``subspecies`` 元素来决定出现的亚种。


subspecies
^^^^^^^^^^^^^^^^^^^

该元素定义了特定的一种亚种类型，其内容应填写一个亚种类型的标识符，详见 :ref:`items-identifier`。

subspeciesToRemove
^^^^^^^^^^^^^^^^^^^^^

该元素定义了特定的一种亚种类型，其内容应填写一个亚种类型的标识符，详见 :ref:`items-identifier`。该元素的作用是在 ``subspeciesPresent`` 元素中定义的亚种中去除该亚种。

示例
~~~~~~~~~~~~~~

下例代表了在该地点类型中会出现一种名为 ``CLERK`` 的人群，人数为几个(``COUPLE``)，该人群永远都会存在，且种族为恶魔。

.. code:: xml

	<populationPresent>
		<population>
			<populationType plural="true" density="COUPLE">CLERK</populationType>
			<subspeciesPresent>
				<subspecies>DEMON</subspecies>
			</subspeciesPresent>
		</population>
	</populationPresent> 

furniturePresent
-------------------

该元素定义了该地点类型是否会出现家具。该元素是 :ref:`optional`，若留空，则代表该地点没有家具(主要指桌子)。

**节点属性:**
    .. nodevar:: [deskName] <string> ()

        属性 ``deskName`` 的数值应填写该地点类型的桌子名称，若留空，则使用的默认桌子名称。

loiteringEnabled
-------------------

该元素决定了玩家是否能够在该地点类型中进行闲逛。该元素的数值为 :ref:`boolean-values`，默认设置为 ``false``。


wallsPresent
-------------------

该元素定义了该地点类型是否存在墙面。该元素是 :ref:`optional`，若留空，则代表该地点没有墙面(如大厅中央)。

**节点属性:**
	.. nodevar:: [wallName] <string> ()

		属性 ``wallName`` 的数值应填写该地点类型的墙面名称，若留空，则使用的默认墙面名称。

globalMapTile
-----------------

该元素定义了该地点类型是否处于全球地图中， *用途不完全清楚*，可能用于表示该地点类型是否属于全球地图中。

dangerous
---------------

该元素定义了该地点类型是否是危险地块，并且会进行 :ref:`parse` ，返回值应为 :ref:`boolean-values`。理论上非 ``true`` 的返回值都会视作 ``false``。

itemsDisappear
----------------

该元素决定了该地点类型中的物品是否会消失。该元素的数值为 :ref:`boolean-values`。

aquatic
-------------

该元素决定了该地点类型的水陆情况，可填入的内容请参见 :ltgithub:`src/com/lilithsthrone/world/places/Aquatic.java`。下面的例子中代表该地点类型是陆地。

.. code:: xml

	<aquatic><![CDATA[LAND]]></aquatic>


darkness
-------------

该元素决定了该地点类型的光照情况，可填入的内容请参见 :ltgithub:`src/com/lilithsthrone/world/places/Darkness.java`。下面的例子中代表该地点类型总是明亮的，若为空字符串，则代表该地点类型的光照情况为日光。

.. code:: xml

	<darkness><![CDATA[ALWAYS_LIGHT]]></darkness>

teleportPermissions
---------------------

该元素决定了该地点类型是否允许传送，可填入的内容请参见 :ltgithub:`src/com/lilithsthrone/world/TeleportPermissions.java`。下面的例子中代表该地点类型即允许传入，也允许传出。

.. code:: xml

	<teleportPermissions>BOTH</teleportPermissions>

weatherImmunities
-------------------

该元素决定了该地点类型免疫哪些天气影响，该元素是 :ref:`optional`，若留空，则代表该地点类型不免疫任何天气影响。每一种天气都将在该元素内以 `weather`_ 标签的形式出现。可以定义多个 ``weather`` 标签。

**节点属性:**
    .. nodevar:: [immuneToAll] <boolean> ()

        属性 ``immuneToAll`` 决定了该地点类型是否免疫所有天气影响。若填写该值，则可以省略 ``weatherImmunities`` 元素内的 ``weather`` 元素。


weather
~~~~~~~~~~~~~

该元素决定了该地点类型免疫的天气类型，可填入的内容请参见 :ltgithub:`src/com/lilithsthrone/world/Weather.java`。


applyInventoryInit
----------------------

该元素决定了该地点类型初始化时地块上的物品，是 :ref:`optional`。尽管本意如此，但若希望通过 :ref:`parse` 来完成其他功能同样可以。在该元素中可以使用特殊的解析对象 ``inventory``，来操作该地块上的物品。下面的例子中代表该地点类型初始化时地块上会出现一本半恶魔的种族书(``BOOK_HALF_DEMON``)。

.. code:: xml

	<applyInventoryInit><![CDATA[
        [##
            var book = game.getItemGen().generateItem(ITEM_BOOK_HALF_DEMON);
            inventory.addItem(book);
        ]
        ]]></applyInventoryInit>
