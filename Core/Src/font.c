#include "font.h"
#include "pcd8544.h"

#define FONT_SEGMENT_SIZE (6)

static uint8_t segments_lookup[] = {
        0b11111111,
};

void font_draw_numbers(pcd8544_handle_t *handle, uint8_t x, uint8_t y, const uint8_t *numbers){
    while(*numbers != 0xff){
        uint8_t segments = segments_lookup[*numbers];

        // A
        for(int i=0; i<FONT_SEGMENT_SIZE;i++){
//            pcd8544_set_pixel(handle, x, y, )
        }

        numbers++;
    }
}
