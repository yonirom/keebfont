BUILD_DIR = build
INTERMEDIATE_DIR = tmp
INTERMEDIATE_OBJECTS = $(INTERMEDIATE_DIR)/Cozette.bdf $(INTERMEDIATE_DIR)/Keebglyphs.bdf
BDF_OBJECTS = $(BUILD_DIR)/Keeb.bdf $(BUILD_DIR)/KeebBold.bdf $(BUILD_DIR)/KeebItalic.bdf 
TTF_OBJECTS = $(BDF_OBJECTS:.bdf=.ttf)
OTB_OBJECTS = $(BDF_OBJECTS:.bdf=.otb)

.PRECIOUS: %.otb

.PHONY: all
all: $(TTF_OBJECTS) | $(BUILD_DIR)

$(BUILD_DIR): | $(INTERMEDIATE_DIR)
	mkdir -p $(BUILD_DIR)

$(INTERMEDIATE_DIR): 
	mkdir -p $(INTERMEDIATE_DIR)

$(INTERMEDIATE_OBJECTS): $(INTERMEDIATE_DIR)/%.bdf : src/%.sfd | $(BUILD_DIR)
	python convert_font_type.py $< $@

$(BDF_OBJECTS): | $(INTERMEDIATE_OBJECTS)
	python build.py

%.otb: %.bdf 
	bitmapfont2otb --no-rename $< $@ 


%.ttf: %.otb
	python convert_font_type.py $< $@
