BUILD_DIR = build
INTERMEDIATE_DIR = build/inter
SOURCE_SFDS = src/Cozette.sfd src/Keebglyphs.sfd
INTERMEDIATE_TARGETS = $(INTERMEDIATE_DIR)/Cozette.bdf $(INTERMEDIATE_DIR)/Keebglyphs.bdf
BDF_TARGETS = $(BUILD_DIR)/Keeb.bdf $(BUILD_DIR)/KeebBold.bdf $(BUILD_DIR)/KeebItalic.bdf 
TTF_TARGETS = $(patsubst %.bdf, %.ttf, $(BDF_TARGETS))
OTB_TARGETS = $(patsubst %.bdf, %.otb, $(BDF_TARGETS))
TARGETS = Keeb.otb KeebBold.otb KeebItalic.otb

.PHONY: all
all: $(TTF_TARGETS) | $(BUILD_DIR)

$(BUILD_DIR): | $(INTERMEDIATE_DIR)
	mkdir -p $(BUILD_DIR)

$(INTERMEDIATE_DIR): 
	mkdir -p $(INTERMEDIATE_DIR)

$(BDF_TARGETS): $(INTERMEDIATE_TARGETS)
	python build.py

$(OTB_TARGETS): $(BDF_TARGETS)
	bitmapfont2otb $< $@

$(INTERMEDIATE_TARGETS): $(SOURCE_SFDS) | $(INTERMEDIATE_DIR)
	python convert_font_type.py $< $@

$(TTF_TARGETS): $(OTB_TARGETS)
	python convert_font_type.py $< $@
