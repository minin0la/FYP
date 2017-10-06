#############################################################################
# Generated by PAGE version 4.9
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top60
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# USER DEFINED PROCEDURES
#

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top60 {base} {
    if {$base == ""} {
        set base .top60
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m80" -background {#d9d9d9} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1024x600+361+161
    update
    # set in toplevel.wgt.
    global vTcl
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1680 1005
    wm minsize $top 72 15
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "FridgeBud"
    vTcl:DefineAlias "$top" "manage_settings" vTcl:Toplevel:WidgetProc "" 1
    button $top.but62 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Set Work Location} 
    vTcl:DefineAlias "$top.but62" "work_set_button" vTcl:WidgetProc "manage_settings" 1
    button $top.cpd63 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Set Weather Location} 
    vTcl:DefineAlias "$top.cpd63" "weather_set_button" vTcl:WidgetProc "manage_settings" 1
    entry $top.cpd65 \
        -background white -font TkFixedFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$top.cpd65" "weather_entry" vTcl:WidgetProc "manage_settings" 1
    entry $top.cpd66 \
        -background white -font TkFixedFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$top.cpd66" "work_entry" vTcl:WidgetProc "manage_settings" 1
    button $top.cpd76 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Home 
    vTcl:DefineAlias "$top.cpd76" "home_button" vTcl:WidgetProc "manage_settings" 1
    menu $top.m80 \
        -activebackground {#d8d8d8} -activeforeground {#000000} \
        -background {#d9d9d9} -font TkMenuFont -foreground {#000000} \
        -tearoff 0 
    button $top.cpd37 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Quit Application} 
    vTcl:DefineAlias "$top.cpd37" "quit_button" vTcl:WidgetProc "manage_settings" 1
    label $top.lab38 \
        -background {#d9d9d9} -foreground {#000000} \
        -text {Current Work Location} 
    vTcl:DefineAlias "$top.lab38" "current_work_label" vTcl:WidgetProc "manage_settings" 1
    label $top.cpd39 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Current Weather Location} 
    vTcl:DefineAlias "$top.cpd39" "current_weather_label" vTcl:WidgetProc "manage_settings" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but62 \
        -in $top -x 80 -y 130 -width 167 -relwidth 0 -height 32 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.cpd63 \
        -in $top -x 80 -y 170 -width 167 -relwidth 0 -height 32 -relheight 0 \
        -anchor nw -bordermode inside 
    place $top.cpd65 \
        -in $top -x 260 -y 170 -width 282 -relwidth 0 -height 27 -relheight 0 \
        -anchor nw -bordermode inside 
    place $top.cpd66 \
        -in $top -x 260 -y 130 -width 282 -relwidth 0 -height 27 -relheight 0 \
        -anchor nw -bordermode inside 
    place $top.cpd76 \
        -in $top -x 800 -y 530 -width 167 -height 32 -anchor nw \
        -bordermode inside 
    place $top.cpd37 \
        -in $top -x 620 -y 530 -width 167 -height 32 -anchor nw \
        -bordermode inside 
    place $top.lab38 \
        -in $top -x 610 -y 130 -width 341 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.cpd39 \
        -in $top -x 610 -y 170 -width 341 -height 24 -anchor nw \
        -bordermode inside 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

Window show .
Window show .top60
