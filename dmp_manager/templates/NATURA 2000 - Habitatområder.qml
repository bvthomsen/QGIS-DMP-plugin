<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis readOnly="0" version="3.16.3-Hannover" maxScale="0" simplifyDrawingHints="1" simplifyLocal="1" simplifyAlgorithm="0" simplifyMaxScale="1" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" minScale="100000000" simplifyDrawingTol="1" labelsEnabled="0">
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
  <renderer-v2 symbollevels="0" forceraster="0" type="singleSymbol" enableorderby="0">
    <symbols>
      <symbol alpha="1" force_rhr="0" clip_to_extent="1" type="fill" name="0">
        <layer enabled="1" locked="0" class="SimpleFill" pass="0">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="164,113,88,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="dense4" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property key="dualview/previewExpressions">
      <value>"objekt-id"</value>
    </property>
    <property value="0" key="embeddedWidgets/count"/>
    <property value="DMPManager" key="variableNames"/>
    <property value="habitat_omr" key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory height="15" scaleDependency="Area" lineSizeScale="3x:0,0,0,0,0,0" diagramOrientation="Up" maxScaleDenominator="1e+08" enabled="0" spacing="5" opacity="1" rotationOffset="270" backgroundColor="#ffffff" backgroundAlpha="255" direction="0" spacingUnitScale="3x:0,0,0,0,0,0" minScaleDenominator="0" minimumSize="0" showAxis="1" penWidth="0" penColor="#000000" labelPlacementMethod="XHeight" sizeType="MM" lineSizeType="MM" barWidth="5" scaleBasedVisibility="0" penAlpha="255" spacingUnit="MM" sizeScale="3x:0,0,0,0,0,0" width="15">
      <fontProperties description="MS Shell Dlg 2,7.8,-1,5,50,0,0,0,0,0" style=""/>
      <attribute color="#000000" label="" field=""/>
      <axisSymbol>
        <symbol alpha="1" force_rhr="0" clip_to_extent="1" type="line" name="">
          <layer enabled="1" locked="0" class="SimpleLine" pass="0">
            <prop v="0" k="align_dash_pattern"/>
            <prop v="square" k="capstyle"/>
            <prop v="5;2" k="customdash"/>
            <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
            <prop v="MM" k="customdash_unit"/>
            <prop v="0" k="dash_pattern_offset"/>
            <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
            <prop v="MM" k="dash_pattern_offset_unit"/>
            <prop v="0" k="draw_inside_polygon"/>
            <prop v="bevel" k="joinstyle"/>
            <prop v="35,35,35,255" k="line_color"/>
            <prop v="solid" k="line_style"/>
            <prop v="0.26" k="line_width"/>
            <prop v="MM" k="line_width_unit"/>
            <prop v="0" k="offset"/>
            <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
            <prop v="MM" k="offset_unit"/>
            <prop v="0" k="ring_filter"/>
            <prop v="0" k="tweak_dash_pattern_on_corners"/>
            <prop v="0" k="use_custom_dash"/>
            <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
            <data_defined_properties>
              <Option type="Map">
                <Option value="" type="QString" name="name"/>
                <Option name="properties"/>
                <Option value="collection" type="QString" name="type"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings zIndex="0" placement="1" dist="0" showAll="1" obstacle="0" priority="0" linePlacementFlags="18">
    <properties>
      <Option type="Map">
        <Option value="" type="QString" name="name"/>
        <Option name="properties"/>
        <Option value="collection" type="QString" name="type"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option type="Map" name="QgsGeometryGapCheck">
        <Option value="0" type="double" name="allowedGapsBuffer"/>
        <Option value="false" type="bool" name="allowedGapsEnabled"/>
        <Option value="" type="QString" name="allowedGapsLayer"/>
      </Option>
    </checkConfiguration>
  </geometryOptions>
  <legend type="default-vector"/>
  <referencedLayers/>
  <fieldConfiguration>
    <field configurationFlags="None" name="objekt-id">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="version-id">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="systid-fra">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="systid-til">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="oprettet">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="oprindkode-id">
      <editWidget type="ValueRelation">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="AllowMulti"/>
            <Option value="false" type="bool" name="AllowNull"/>
            <Option value="" type="QString" name="Description"/>
            <Option value="" type="QString" name="FilterExpression"/>
            <Option value="key" type="QString" name="Key"/>
            <Option value="oprindkode_id_42e0b7fe_cc5e_4805_bd44_35940c535849" type="QString" name="Layer"/>
            <Option value="oprindkode-id" type="QString" name="LayerName"/>
            <Option value="memory" type="QString" name="LayerProviderName"/>
            <Option value="None&amp;uid={5ac7cebc-876c-4d10-b393-f39c4ccc7db7}" type="QString" name="LayerSource"/>
            <Option value="1" type="int" name="NofColumns"/>
            <Option value="false" type="bool" name="OrderByValue"/>
            <Option value="false" type="bool" name="UseCompleter"/>
            <Option value="value" type="QString" name="Value"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="statuskode-id">
      <editWidget type="ValueRelation">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="AllowMulti"/>
            <Option value="false" type="bool" name="AllowNull"/>
            <Option value="" type="QString" name="Description"/>
            <Option value="" type="QString" name="FilterExpression"/>
            <Option value="key" type="QString" name="Key"/>
            <Option value="statuskode_id_690eae4c_9bc7_4d34_8c40_a33973e58fa4" type="QString" name="Layer"/>
            <Option value="statuskode-id" type="QString" name="LayerName"/>
            <Option value="memory" type="QString" name="LayerProviderName"/>
            <Option value="None&amp;uid={ceb65c87-f6a7-4421-9115-2de29576ebc1}" type="QString" name="LayerSource"/>
            <Option value="1" type="int" name="NofColumns"/>
            <Option value="false" type="bool" name="OrderByValue"/>
            <Option value="false" type="bool" name="UseCompleter"/>
            <Option value="value" type="QString" name="Value"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="off-kode-id">
      <editWidget type="ValueRelation">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="AllowMulti"/>
            <Option value="false" type="bool" name="AllowNull"/>
            <Option value="" type="QString" name="Description"/>
            <Option value="" type="QString" name="FilterExpression"/>
            <Option value="key" type="QString" name="Key"/>
            <Option value="off_kode_id_abae66e6_cfa0_43ea_9455_ca370623bdc0" type="QString" name="Layer"/>
            <Option value="off-kode-id" type="QString" name="LayerName"/>
            <Option value="memory" type="QString" name="LayerProviderName"/>
            <Option value="None&amp;uid={ac531b85-0b18-44dd-aba4-4c337bcc112d}" type="QString" name="LayerSource"/>
            <Option value="1" type="int" name="NofColumns"/>
            <Option value="false" type="bool" name="OrderByValue"/>
            <Option value="false" type="bool" name="UseCompleter"/>
            <Option value="value" type="QString" name="Value"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cvr-kode-id">
      <editWidget type="ValueRelation">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="AllowMulti"/>
            <Option value="false" type="bool" name="AllowNull"/>
            <Option value="" type="QString" name="Description"/>
            <Option value="" type="QString" name="FilterExpression"/>
            <Option value="key" type="QString" name="Key"/>
            <Option value="cvr_kode_id_21547e69_7524_4296_b185_d2d48b00529f" type="QString" name="Layer"/>
            <Option value="cvr-kode-id" type="QString" name="LayerName"/>
            <Option value="memory" type="QString" name="LayerProviderName"/>
            <Option value="None&amp;uid={a65ee476-d0e6-4a74-85be-65e0a40f9558}" type="QString" name="LayerSource"/>
            <Option value="1" type="int" name="NofColumns"/>
            <Option value="false" type="bool" name="OrderByValue"/>
            <Option value="false" type="bool" name="UseCompleter"/>
            <Option value="value" type="QString" name="Value"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="bruger-id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="link">
      <editWidget type="ExternalResource">
        <config>
          <Option type="Map">
            <Option value="2" type="int" name="DocumentViewer"/>
            <Option value="0" type="int" name="DocumentViewerHeight"/>
            <Option value="0" type="int" name="DocumentViewerWidth"/>
            <Option value="true" type="bool" name="FileWidget"/>
            <Option value="false" type="bool" name="FileWidgetButton"/>
            <Option value="" type="QString" name="FileWidgetFilter"/>
            <Option value="true" type="bool" name="FullUrl"/>
            <Option type="Map" name="PropertyCollection">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
            <Option value="0" type="int" name="RelativeStorage"/>
            <Option value="0" type="int" name="StorageMode"/>
            <Option value="true" type="bool" name="UseLink"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="shape">
      <editWidget type="Hidden">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="site-nr">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="objektnavn">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="loc-ident">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="site-ident">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="gyldig-fra">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="gyldig-til">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" field="objekt-id" name="ObjektId"/>
    <alias index="1" field="version-id" name="VersionId"/>
    <alias index="2" field="systid-fra" name="Start systemtid"/>
    <alias index="3" field="systid-til" name="Slut systemtid"/>
    <alias index="4" field="oprettet" name="Systemtid for oprettelse"/>
    <alias index="5" field="oprindkode-id" name="Oprindelse"/>
    <alias index="6" field="statuskode-id" name="Gældende status"/>
    <alias index="7" field="off-kode-id" name="Tilgængelighed"/>
    <alias index="8" field="cvr-kode-id" name="Myndighed"/>
    <alias index="9" field="bruger-id" name="Brugere"/>
    <alias index="10" field="link" name="URL-link"/>
    <alias index="11" field="shape" name="Shape"/>
    <alias index="12" field="site-nr" name="SiteNr (Kodeværdi for GIS objekt)"/>
    <alias index="13" field="objektnavn" name="Objektnavn"/>
    <alias index="14" field="loc-ident" name="SPA + identifikation af objektet"/>
    <alias index="15" field="site-ident" name="Officiel EU Sitecode fra bekendtgørelse"/>
    <alias index="16" field="gyldig-fra" name="Start på gyldighedsperiode"/>
    <alias index="17" field="gyldig-til" name="Slut på gyldighedsperiode"/>
  </aliases>
  <defaults>
    <default expression="" applyOnUpdate="0" field="objekt-id"/>
    <default expression="" applyOnUpdate="0" field="version-id"/>
    <default expression="" applyOnUpdate="0" field="systid-fra"/>
    <default expression="" applyOnUpdate="0" field="systid-til"/>
    <default expression="" applyOnUpdate="0" field="oprettet"/>
    <default expression="" applyOnUpdate="0" field="oprindkode-id"/>
    <default expression="" applyOnUpdate="0" field="statuskode-id"/>
    <default expression="" applyOnUpdate="0" field="off-kode-id"/>
    <default expression="" applyOnUpdate="0" field="cvr-kode-id"/>
    <default expression="" applyOnUpdate="0" field="bruger-id"/>
    <default expression="" applyOnUpdate="0" field="link"/>
    <default expression="" applyOnUpdate="0" field="shape"/>
    <default expression="" applyOnUpdate="0" field="site-nr"/>
    <default expression="" applyOnUpdate="0" field="objektnavn"/>
    <default expression="" applyOnUpdate="0" field="loc-ident"/>
    <default expression="" applyOnUpdate="0" field="site-ident"/>
    <default expression="" applyOnUpdate="0" field="gyldig-fra"/>
    <default expression="" applyOnUpdate="0" field="gyldig-til"/>
  </defaults>
  <constraints>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="objekt-id" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="version-id" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="systid-fra" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="systid-til" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="oprettet" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="oprindkode-id" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="statuskode-id" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="off-kode-id" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="cvr-kode-id" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="bruger-id" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="link" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="shape" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="site-nr" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="objektnavn" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="loc-ident" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="site-ident" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="gyldig-fra" constraints="0"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" field="gyldig-til" constraints="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="objekt-id"/>
    <constraint exp="" desc="" field="version-id"/>
    <constraint exp="" desc="" field="systid-fra"/>
    <constraint exp="" desc="" field="systid-til"/>
    <constraint exp="" desc="" field="oprettet"/>
    <constraint exp="" desc="" field="oprindkode-id"/>
    <constraint exp="" desc="" field="statuskode-id"/>
    <constraint exp="" desc="" field="off-kode-id"/>
    <constraint exp="" desc="" field="cvr-kode-id"/>
    <constraint exp="" desc="" field="bruger-id"/>
    <constraint exp="" desc="" field="link"/>
    <constraint exp="" desc="" field="shape"/>
    <constraint exp="" desc="" field="site-nr"/>
    <constraint exp="" desc="" field="objektnavn"/>
    <constraint exp="" desc="" field="loc-ident"/>
    <constraint exp="" desc="" field="site-ident"/>
    <constraint exp="" desc="" field="gyldig-fra"/>
    <constraint exp="" desc="" field="gyldig-til"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" sortExpression="" actionWidgetStyle="dropDown">
    <columns>
      <column width="-1" hidden="0" type="field" name="objekt-id"/>
      <column width="-1" hidden="0" type="field" name="version-id"/>
      <column width="-1" hidden="0" type="field" name="systid-fra"/>
      <column width="-1" hidden="0" type="field" name="systid-til"/>
      <column width="-1" hidden="0" type="field" name="oprettet"/>
      <column width="-1" hidden="0" type="field" name="oprindkode-id"/>
      <column width="-1" hidden="0" type="field" name="statuskode-id"/>
      <column width="-1" hidden="0" type="field" name="off-kode-id"/>
      <column width="-1" hidden="0" type="field" name="cvr-kode-id"/>
      <column width="-1" hidden="0" type="field" name="bruger-id"/>
      <column width="-1" hidden="0" type="field" name="link"/>
      <column width="-1" hidden="0" type="field" name="shape"/>
      <column width="-1" hidden="0" type="field" name="site-nr"/>
      <column width="-1" hidden="0" type="field" name="objektnavn"/>
      <column width="-1" hidden="0" type="field" name="loc-ident"/>
      <column width="-1" hidden="0" type="field" name="site-ident"/>
      <column width="-1" hidden="0" type="field" name="gyldig-fra"/>
      <column width="-1" hidden="0" type="field" name="gyldig-til"/>
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
    <field editable="1" name="bruger-id"/>
    <field editable="1" name="cvr-kode-id"/>
    <field editable="1" name="gyldig-fra"/>
    <field editable="1" name="gyldig-til"/>
    <field editable="1" name="link"/>
    <field editable="1" name="loc-ident"/>
    <field editable="1" name="objekt-id"/>
    <field editable="1" name="objektnavn"/>
    <field editable="1" name="off-kode-id"/>
    <field editable="1" name="oprettet"/>
    <field editable="1" name="oprindkode-id"/>
    <field editable="0" name="shape"/>
    <field editable="1" name="site-ident"/>
    <field editable="1" name="site-nr"/>
    <field editable="1" name="statuskode-id"/>
    <field editable="1" name="systid-fra"/>
    <field editable="1" name="systid-til"/>
    <field editable="1" name="version-id"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="bruger-id"/>
    <field labelOnTop="0" name="cvr-kode-id"/>
    <field labelOnTop="0" name="gyldig-fra"/>
    <field labelOnTop="0" name="gyldig-til"/>
    <field labelOnTop="0" name="link"/>
    <field labelOnTop="0" name="loc-ident"/>
    <field labelOnTop="0" name="objekt-id"/>
    <field labelOnTop="0" name="objektnavn"/>
    <field labelOnTop="0" name="off-kode-id"/>
    <field labelOnTop="0" name="oprettet"/>
    <field labelOnTop="0" name="oprindkode-id"/>
    <field labelOnTop="0" name="shape"/>
    <field labelOnTop="0" name="site-ident"/>
    <field labelOnTop="0" name="site-nr"/>
    <field labelOnTop="0" name="statuskode-id"/>
    <field labelOnTop="0" name="systid-fra"/>
    <field labelOnTop="0" name="systid-til"/>
    <field labelOnTop="0" name="version-id"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>"objekt-id"</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
