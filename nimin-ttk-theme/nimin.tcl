# Theme uses https://github.com/TkinterEP/ttkthemes/tree/master/ttkthemes/themes/smog as a base

package require Tk

namespace eval ttk::theme::nimin {

    package provide ttk::theme::nimin 0

    set imgdir [file join [file dirname [info script]] images/png]
    proc LoadImages {imgdir {patterns {*.png}}} {
        foreach pattern $patterns {
            foreach file [glob -directory $imgdir $pattern] {
                set img [file tail [file rootname $file]]
                if {![info exists images($img)]} {
                    set images($img) [image create photo -file $file -format png]
                }
            }
        }
        return [array get images]
    }

    array set I [LoadImages \
                     [file join [file dirname [info script]] images/png] *.png]

    variable colors
    array set colors {
        -stage          "#ffffff"
        -borders        "#000000"
        -text           "#000000"
    }


    ttk::style theme create nimin -settings {
        ttk::style configure . \
            -background         $colors(-stage) \
            -foreground         $colors(-text) \
            -bordercolor        $colors(-borders) \
            -font               TkDefaultFont

        ttk::style configure Vertical.TScrollbar -borderwidth 0
        ttk::style layout Vertical.TScrollbar {
            Vertical.Scrollbar.trough -sticky ns -children {
                Scrollbar.uparrow -side top
                Scrollbar.downarrow -side bottom
                Vertical.Scrollbar.thumb -side top -expand true -sticky ns -children {
                    Vertical.Scrollbar.grip -side left -sticky ew
                }
            }
        }

        ttk::style configure Horizontal.TScrollbar -borderwidth 0
        ttk::style layout Horizontal.TScrollbar {
            Horizontal.Scrollbar.trough -children {
                Scrollbar.leftarrow -side left
                Scrollbar.rightarrow -side right
                Horizontal.Scrollbar.thumb -side left -expand true -sticky we -children {
                    Horizontal.Scrollbar.grip -side bottom -sticky ns
                }
            }
        }

        ttk::style configure TButton -anchor center
        ttk::style layout TButton {
            Button.button -children {
                Button.focus -children {
                    Button.padding -children {
                        Button.label
                    }
                }
            }
        }

        #ttk:style latout TNotebook {
        #    Notebook.tab -children {
        #        Notebook.padding -children {
        #            Notebook.focus -children {
        #                Notebook.label
        #            }
        #        }
        #    }
        #}
        ttk::style element create button image \
            [list $I(button-a) \
                pressed $I(button-p) \
                {selected active} $I(button-s) \
                selected $I(button-s) \
                active $I(button-a) \
                disabled $I(button-a)
            ] -border 1 -padding 1 -sticky news
        ttk::style configure Tbutton -padding {4 0 4 0}

        #Fix padding on notebook
        #ttk::style element create Notebook.client \
        #    image $I(surface) -border 2 -sticky news
        ttk::style element create Notebook.tab image \
            [list $I(tab) \
                selected $I(tab-s) \
                active $I(tab-a) \
            ] -border {3 6 3 12} -padding {3 3}

        ttk::style element create Horizontal.Scrollbar.trough image $I(sb-trough) -border 1

        ttk::style element create Horizontal.Scrollbar.thumb image \
            [list $I(sb-thumb-a) \
                selected $I(sb-thumb-s) \
                pressed $I(sb-thumb-p) \
                active $I(sb-thumb-a) \
                disabled $I(sb-thumb) \
            ] -border 12 -padding {8 3}

        ttk::style element create Horizontal.Scrollbar.grip image \
            [list $I(sb-grip-a) \
                active $I(sb-grip-a) \
                disabled $I(sb-grip)
            ]

        ttk::style element create Vertical.Scrollbar.trough image $I(sb-vtrough) -border 1

        ttk::style element create Vertical.Scrollbar.thumb image \
            [list $I(sb-vthumb-a) \
                pressed $I(sb-vthumb-p) \
                selected $I(sb-vthumb-s) \
                {!disabled active} $I(sb-vthumb-a) \
                disabled $I(sb-vthumb) \
            ] -border 12 -padding {3 8}

        ttk::style element create Vertical.Scrollbar.grip image \
            [list $I(sb-vgrip-a) \
                active $I(sb-vgrip-a) \
                disabled $I(sb-vgrip)
            ]

        foreach dir {up down left right} {
            ttk::style element create ${dir}arrow image \
                [list $I(arrow${dir}-a) \
                    disabled $I(arrow${dir}) \
                    pressed $I(arrow${dir}-p) \
                    active $I(arrow${dir}-a) \
                    selected $I(arrow${dir}-s) \
                ] -border 1 -sticky {}
        }
    }
}
