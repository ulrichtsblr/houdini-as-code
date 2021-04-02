# **Creating a donut in less than 10 seconds**

<br>

### The hype

Following the current [donut tutorial][donut] hype, we decided to follow up, and try to make a donut in the shortest time possible.

### The people

A developer who want to learn Houdini & an architect who wants to learn how to program python.

### The workflow

We will be using [Linux][Linux] with [Side FX Houdini][Houdini], [VScode][Vscode], [Python][Python] & [Shell script][Shell script]. Not at any point will we alter the setup through the Houdini UI.

### The status quo

The current render  ![][donut current render]

The current time:    
`5 sec`

The current machine:    
`intel i7` , `rtx 2060`, `16GB ram`

### The evaluation citeria

Validation happens through a Tensorflow model that was trained on 500 scraped [donut images][scraped donut images]. The ouput of the render results in either `yes` or `no`. 

Is this a donut yet?    
# `no`


[Vscode]: https://code.visualstudio.com/
[scraped donut images]: https://www.google.com/search?q=3d+donut+tutorial+blenderguru&tbm=isch&ved=2ahUKEwiGjrzdr8nvAhXU5LsIHczjBdgQ2-cCegQIABAA&oq=3d+donut+tutorial+blenderguru&gs_lcp=CgNpbWcQA1AAWABgzbQBaABwAHgAgAEAiAEAkgEAmAEAqgELZ3dzLXdpei1pbWc&sclient=img&ei=7mtbYIbfOtTJ7_UPzMeXwA0&bih=784&biw=1261&safe=active
[Linux]: https://www.linux.org/
[Houdini]: https://www.sidefx.com/
[Python]: https://www.python.org/
[Shell script]: https://www.shellscript.sh/
[donut]: https://www.google.com/search?q=donut+tutorial+blender&safe=active&sxsrf=ALeKk03gwyEqkmRATzMAF9rpeET1k-E3Kg%3A1616601499643&ei=m2FbYLfYJpDCkwXv4oqQDg&oq=donut+tutorial+blender&gs_lcp=Cgdnd3Mtd2l6EAMyAggAMgIIADIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgjELADECc6BwgAEEcQsAM6BAgjECc6CAgAEBYQChAeUJ4pWL0vYMcwaAFwAngAgAFjiAHcBJIBATmYAQCgAQGqAQdnd3Mtd2l6yAEJwAEB&sclient=gws-wiz&ved=0ahUKEwj3kYTxpcnvAhUQ4aQKHW-xAuIQ4dUDCA0&uact=5
[donut current render]: https://github.com/baudhaus/houdini-as-code/blob/master/media/render.png