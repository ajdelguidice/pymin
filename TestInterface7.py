from apysc import Stage, Sprite, display_on_jupyter

window:Stage = Stage(stage_width=1176, stage_height=662, background_color="#000000")

sprite1 = Sprite()
sprite1.graphics.begin_fill(color="#fff")
sprite1.graphics.draw_rect(x=50, y=50, width=50, height=50)

display_on_jupyter()