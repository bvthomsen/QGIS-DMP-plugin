<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis readOnly="0" version="3.16.3-Hannover" maxScale="0" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" minScale="1e+08">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal durationField="" accumulate="0" enabled="0" mode="0" startExpression="" endExpression="" startField="" fixedDuration="0" durationUnit="min" endField="">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <customproperties>
    <property value="&quot;operation&quot;" key="dualview/previewExpressions"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property value="DMPManager" key="variableNames"/>
    <property value="Requestlog" key="variableValues"/>
  </customproperties>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <legend type="default-vector"/>
  <referencedLayers/>
  <fieldConfiguration>
    <field configurationFlags="None" name="operation">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="url">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="true" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="package">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="true" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="status_code">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="dict">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="true" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="timestamp">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="module">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" field="operation" name=""/>
    <alias index="1" field="url" name=""/>
    <alias index="2" field="package" name=""/>
    <alias index="3" field="status_code" name=""/>
    <alias index="4" field="dict" name=""/>
    <alias index="5" field="timestamp" name=""/>
    <alias index="6" field="module" name=""/>
  </aliases>
  <defaults>
    <default expression="" applyOnUpdate="0" field="operation"/>
    <default expression="" applyOnUpdate="0" field="url"/>
    <default expression="" applyOnUpdate="0" field="package"/>
    <default expression="" applyOnUpdate="0" field="status_code"/>
    <default expression="" applyOnUpdate="0" field="dict"/>
    <default expression="" applyOnUpdate="0" field="timestamp"/>
    <default expression="" applyOnUpdate="0" field="module"/>
  </defaults>
  <constraints>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="operation" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="url" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="package" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="status_code" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="dict" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="timestamp" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="module" constraints="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="operation"/>
    <constraint exp="" desc="" field="url"/>
    <constraint exp="" desc="" field="package"/>
    <constraint exp="" desc="" field="status_code"/>
    <constraint exp="" desc="" field="dict"/>
    <constraint exp="" desc="" field="timestamp"/>
    <constraint exp="" desc="" field="module"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" sortExpression="" actionWidgetStyle="dropDown">
    <columns>
      <column width="-1" hidden="0" type="field" name="operation"/>
      <column width="171" hidden="0" type="field" name="url"/>
      <column width="-1" hidden="0" type="field" name="package"/>
      <column width="-1" hidden="0" type="field" name="status_code"/>
      <column width="177" hidden="0" type="field" name="dict"/>
      <column width="-1" hidden="0" type="field" name="timestamp"/>
      <column width="-1" hidden="0" type="field" name="module"/>
      <column width="-1" hidden="1" type="actions"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field editable="1" name="dict"/>
    <field editable="1" name="module"/>
    <field editable="1" name="operation"/>
    <field editable="1" name="package"/>
    <field editable="1" name="status_code"/>
    <field editable="1" name="timestamp"/>
    <field editable="1" name="url"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="dict"/>
    <field labelOnTop="0" name="module"/>
    <field labelOnTop="0" name="operation"/>
    <field labelOnTop="0" name="package"/>
    <field labelOnTop="0" name="status_code"/>
    <field labelOnTop="0" name="timestamp"/>
    <field labelOnTop="0" name="url"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>"operation"</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>4</layerGeometryType>
</qgis>
