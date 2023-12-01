.. include:: global.inc.rst
============
偶遇事件
============

    :Authors: innoxia, CK_Rainbow, AceXP

偶遇事件(Encounters)即在地图上行进过程中，会随机或固定触发的事件。

你可以在 :ltgithub:`res/encounters/` 文件夹中找到正在使用的偶遇事件。

通用信息
--------------

在xml文件中，根元素的标签需要设置为 ``encounterRoot``。

偶遇事件一般用于添加随机风味事件；或者用于覆盖对应地点类型的内置对话，以达成触发额外对话链的功能。

additionalPlaceTypeTrigger
---------------------------

该元素下的内容代表了该偶遇事件可能触发的地点类型。每一种类型都需要使用 ``placeType`` 元素包裹。在此处定义的地点类型对于其下定义的偶遇事件通用。

placeType
~~~~~~~~~~~

对于 ``placeType`` 中可以填入的内容，请参见 :ref:`items-identifier`。下面的例子中代表该偶遇事件只会在 ``ANGELS_KISS_OFFICE`` 中检测触发。

.. code:: xml

    <additionalPlaceTypeTriggers>
        <placeType>ANGELS_KISS_OFFICE</placeType>
    </additionalPlaceTypeTriggers>

possibleEncounters
-----------------------------

该元素下的内容即偶遇事件的具体定义。每一种偶遇事件都将由对应的 `encounter`_ 元素定义。可以定义多个 ``encounter`` 元素。

encounter
~~~~~~~~~~~~~

该元素中定义了单个偶遇事件的具体内容。

name
^^^^^^^

该元素定义了偶遇事件的名称。目前该名称仅用于debug。

chanceToTrigger
^^^^^^^^^^^^^^^^^^

该元素定义了这个偶遇事件的触发概率，并且会进行 :ref:`parse`，达成依照不同条件调整概率的功能。在该部分中，无法使用 ``npc`` 等作为解析主体。若返回0则代表无法触发。

**节点属性:**
    .. nodevar:: opportunisticEncounter <boolean> ()

        属性 ``opportunisticEncounter`` 必须填写， ``false`` 代表该偶遇事件不受“机会主义”的影响，不会受到权重加成，反之则受影响。

下例展示了一个十分复杂的概率判定，以展示其能力。

.. code:: xml

    <chanceToTrigger opportunisticEncounter="false"><![CDATA[
        #IF(!game.isStarted() || flags.hasFlag(FLAG_acexp_horny_angel_found) || !flags.hasFlag(FLAG_angelsOfficeIntroduced) || !flags.hasFlag(FLAG_prostitutionLicenseObtained))
            0
        #ELSE
            100
        #ENDIF
    ]]></chanceToTrigger>

dialogueReturned
^^^^^^^^^^^^^^^^^

该元素定义了这个偶遇事件触发后，游戏将会调用哪个对话。对于其中中可以填入的内容，请参见 :ref:`items-identifier`。

.. code:: xml

    <dialogueReturned><![CDATA[acexp_dominion_angel_office_horny_angel]]></dialogueReturned>