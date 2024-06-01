# Simple Retarded YouTube Playlist Downloader Using PipedAPI
ᵒʳ ˢᴿʸᴾᴰᵁᴾ ᶠᵒʳ ˢʰᵒʳᵗ :⁾


Hello guys this is a simple youtube playlist downloader by me.

**It currently (as of 2024/6/1) sucks a bit because the API I use for downloading stuff is currently facing some kind of outage.**

**Don't expect it to work too well right now**

#### Update:
At the time this commit is pushed, I have found a working alternative PipedAPI instance. Use the following baseUrl for now:
> https://pipedapi.syncpundit.io

#### How to use:
1. Download [`FFMPEG`](https://ffmpeg.org/download.html)
2. Run `main.py`
3. I guess that's it. Just follow the instructions.


I am using [Piped](https://github.com/TeamPiped/Piped) for this. Documents for its API can be found here: https://github.com/TeamPiped/Piped

### TODO LIST
- [X] Do the todo list
- [ ] Stop the damn thing from closing when downloads are done (easiest task, but I will do this next time)
- [ ] Allow user to set range to download using the index (instead of downloading the whole playlist from the start)
- [ ] Add logging of all output to a text file
- - [ ] Also make error logs a separate file
- [ ] Threading. Yes.
- [ ] Use Inviduous API instead, if Piped is still constantly down

```
*%%%%%%%%%%###############%%%@@@@@@@+   ..          -@@@@@@@@@@@@@@@@.   ..          
*@@@%%%%%%%@@@@@@@@@@@@@@@@@@@@.  . .:---::::-:::::..    @@@@@@.     .==-:---=+==+=* 
+%%%%@@%@%%%%%%%%%%%%@@@@@@@  ..::=::-::--:-::.--......:.    .:+#%@*=--==+=------=.  
*%%@%%%%%%%%%%@%@@@@%@@@@.  .--::--:.::::::::---:--::.........=@@-::=-=:.:=+===:     
+%%%@@@@@%%%%%%@@%%@@@@  :::----==:-::::::---:::::::.:::::::....:--:..:-::=:.        
+%%%%%%%%%@@%%%@%@@@@  ::.:--+----:::----:.....::.::..............@@%=+.       *@@@@@
=%%#@%%%%%%%@@@%@@@ ..-=----:==---::..::::..:::....:.............. %@ :@@@@@@@@@@@@@#
=%%%%%%%%%%%%%%%@@..++======+=-:::-:..::::-:::::....:......-....... =@@@@@@@@@@@@@@@%
=%%%%%%%%%%%%#%%@:.+==++*+=====--:------------::-:::.:.............. @@@@@@@@@@@@@@@%
=%%%%%%%%%%%%%%@@.-++======+==+=---:-------:::::::::.:.............. @@@@@@@%-:....  
=%%%%%%%%%%%%%@@..+**====-++++======---------::.::.:.................      .@+*#*=%. 
=%%%%%%%%%%%%%@=.--====+=--===---==-------::::::::...::...............%+=--..@%#*#@. 
=%%%%%%%%%%%@@@ :*=-++=+=++=--===+=-=-------:::----::................ *:@=.:..*@*+@  
=%%%%%%%%@@@@@@+###*+:*#*=------====++++=====--::::.::.:............. +.@*.... .@*@  
=%%%%%%@@@     %***++=*+==-----::::.:....::::-:::::...:-::..........: @@@##%#**=-@@  
=%%%%%%@:.*#@@. .++++++==+++===-:............::::::....:::-:......... = *@@@@@@@@@@- 
=%%%%%@@ =#*+ %-.%#====-==---::...=+@@@@@*:.  ....:..::....::::::::.: @@@# @...      
+%%%%%@@ %.  +.-*==-=:-:-::-:=*#@@@@@@@@@@@@@@:...---::::::::::::.... @+@  @@@@@@@@@@
+%%%%@@@ =-:@@@.-:+====-=---+***=::::::--:-+%@@@@%#+-.:::::::::.......@*@: @@@@@@%*..
+%@@@@@@ =+.@%%.:-*=---===-:-=-=..::-.:.....:**+@@@%##+-::-::::..... @@:@  @@***#@- -
#@@@%@@@-:#%%#%---++=--:--=#*+*##@@@@@@@@@@@+ -@%**+**-::---:....=:+=@@:@. @%##%%@+ *
*%@@@@%@@ .#  +=-=-=+=+=::--=+==-*+=*%. @@@@@:@.@@%%#*=--::...*@@@@@@%@#@  @@%###@= =
*%@@@@@@@# :+ :=:+++++=-:----:.::::..+#+.    .#::#-.:==:..  +%+.....@@@@@  @@@@@@@=. 
#@@@@@@@@@. ..+-:++=++=------::...:--.:+*%%%#:  .+=:----:. =@@@+@*..             @=. 
#@@@@@@@@@@.  @#+==+=+:-==---:-::.........:::::-------:--. .  @@ @@@@@@@@@:--:...@-* 
#@@@@@@@@@@@@@@-:==---=++=-=--::::::-:----:::...:::::---=. :++=.@@@@@@@@@@%@@@@@@@@@:
#@@@@@@@@@@@@@.====+++++++++--:::-:-----:......::-::::::-: .-=: .    ......::---.-== 
#@@@@@@@@@@@@= =+==+=======+==-:::::.....::::-:::-:--::--:...-..:::::-.++@%#**#%##*+ 
#@@@@@@@@@@@@ -+=+===+=-====++=-:-:::::::::::---=------==-...:.*%+##-*==-..::::..... 
%@@@@@@@@@@@:.*===++==++-===+*+==-:::::::::::-:-====--=---...:.*:-:--=-:+=====---::- 
#@@@@@@@@@@@ :=#=====+%*=+=--====---:::::::::::-::-::...... ..---==--------=::==*:++.
#@%%%%@@@@@ :==#===++++===+==---------::::--::::...:::::.:.  .-=-:-----+*%%@@@@#%@%-.
#%@@@@@%@@..+==@%*+=++==+#*------------::..+@.   ......:::... -:---::-:=..         . 
*%%%@@@@@@ :===*@##*+=+***+*#++===-:-:----:.@@@@+.  ......... .+:---:@=     :+==::.. 
@@@@@@@=. .-+=+=+###*+=-=++=-:=-=-=-------:..=@@@@@@+:.:......:===*#%%@@@@@=.      . 
.       ..::-=+==##**####*+-=-=-=------:::-:.....:*@@@@@@##**+*==-:..::- -#@@@@@@@@% 
.:-@*..:---==+*+-=%@**#****+====-:::..::...:::::... .   ++-:===----::....:......:+@@=
.@%..:-:::---=++==:@%#***+==--+-:-=-----===----==:-=#+::..@@::::-:::::---::.:--....  
.@.-:::::----+=--+==%#****%*==+++==-....:::::::.........:  :-#@..   ..:---+=...:::.- 
...:::::::::.=+--=-=+#**+=+*+=*+##*+@@@@@#+:.         .+%==-::-+@@@@.      .:--+-::- 
.---:.:::-:::-=--===+*#*+==****++=+-.. .+%@@@@@@@@@%%####=---::.  .@@@@@@@=       := 
:*-=-:::::..--:-::-=:-+*%#+*%###**=+=-=:..:. .    ...:=---::::--:::  .@@@@@@@@@@@:   
.@:.::.::...:-::.:---:::=*%++###%%*+++*++=-:.: . ..-++=::.:::.:---:--. .@@@@@@@@@@@@@
.-@+:::..........:---.:===-%*==+=#@@*#@@@@@@@@@@%@@----=--:....:.:.-=-:.: @@@@@@@@@@#
.-:@+:------:---::--=:.-=+=-*#+-. :*+====-::---:. =---:-::---.:--====--..=- -@@@@@@@#
.  ..                    .   .....                                        ..    *###*

```
© JohnTWD Technologies™ LLC. All rights reserverd®

Jk...you are free too do whatever you want with this. Though of course, credit me as the original author :^)

Yes I am very unfunny
