screen world_map:
    frame:
        align (0.5, 0.5)
        imagemap:
            idle "map.png"
            hover "map-hover.png"
        
            hotspot (323, 134, 22, 23) clicked Jump("new_paris")
            hotspot (344, 292, 20, 22) clicked Jump("capital_city")
            hotspot (171, 269, 26, 24) clicked Jump("lavenoir")
            hotspot (509, 472, 22, 21) clicked Jump("scraptown")

screen map_button:
    frame:
        align (0.75, 0.1)
        textbutton _("Карта") action Show("world_map")