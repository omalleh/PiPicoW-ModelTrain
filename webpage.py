# Setup Webpage
def webpage(showDirection, showSpeed, tacho):
    html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
            <script src="https://kit.fontawesome.com/5e44773cc2.js" crossorigin="anonymous"></script>
            </head>
            <body>
            <table>
            <thead>
                <tr>
                    <td colspan="2">Lights</td>
                    <td></td>
                    <td> Direction </td>
                    <td> Speedometer </td>
                    <td> Acclerometer </td>
                </tr>
              <tr>
                <td><i class="fa-light fa-sun"></i></td>
                <td>
                    <form action='./day'>
                        <input type='submit' value='day' />
                    </form>
                </td>
                <td></td>
                <td><i class="fa-light fa-up"></i></td>
                <td><i class="fa-light fa-gauge-high"></i></td>
                <td rowspan="4">
                    <div class="sc-gauge">
                        <div class="sc-background">
                          <div class="sc-percentage"></div>
                          <div class="sc-mask"></div>
                        <span class="sc-value">{tacho}</span>
                        </div>
                        <span class="sc-min">0</span>
                        <span class="sc-max">100</span>
                    </div>
                </td>
                <td rowspan="4">
                    <form id='form'>
                        <input type='range' class='slider' min='0' max='9' value='{showSpeed}' name='motor' id='motor'>
                    </form>
                </td>
              </tr>
              <tr>
                <td><i class="fa-light fa-moon"></i></td>
                <td>
                    <form action='./night'>
                        <input type='submit' value='night' />
                    </form>
                </td>
                <td></td>
                <td>
                    <form action='./forward'>
                        <input type='submit' value='forward' />
                    </form>
                </td>
                <td>{showDirection}</td>
              </tr>
              <tr>
                <td><i class="fa-light fa-lightbulb"></i></td>
                <td>
                    <form action='./coach'>
                        <input type='submit' value='coach' />
                    </form>
                </td>
                <td></td>
                <td>
                    <form action='./reverse'>
                        <input type='submit' value='reverse' />
                    </form>
                </td>
                <td>{showSpeed}</td>
              </tr>
              <tr>
                <td><i class="fa-light fa-octagon-exclamation"></i></td>
                <td>
                    <form action='./off'>
                        <input type='submit' value='off' />
                    </form>
                </td>
                <td></td>
                <td><i class="fa-light fa-down"></i></td>
                <td><output></output></td>
              </tr>
            </thead>
            </table>
            
            <script>
            let i = document.getElementById('motor'),
                o = document.querySelector('output');

            o.innerHTML = i.value;

            i.addEventListener('input', function () {{
              o.innerHTML = i.value;
            }}, false);
            
            i.addEventListener('change', function ()  {{
                document.getElementById('form').submit();
            }}, false);
            </script>
            <style>
            body{{
                font-family: 'Roboto', sans-serif;
            }}
            input[type="submit"] {{
               width:100px;
               height:100px;
            }}
            td {{
                text-align: center; 
                vertical-align: middle;
            }}
            input[type="range"] {{
               transform: rotate(270deg);
            }}
            .slider {{
              -webkit-appearance: none;
              width: 400px;
              height: 15px;
              border: 2px solid rgb(149, 165, 166);
              border-radius: 5px;  
              background: rgb(189, 195, 199);
              outline: none;
              opacity: 0.7;
              -webkit-transition: .2s;
              transition: opacity .2s;
            }}
            .slider::-webkit-slider-thumb {{
              -webkit-appearance: none;
              appearance: none;
              width: 100px;
              height: 100px;
              border-radius: 50%; 
              background: rgb(44, 62, 80);
              cursor: pointer;
            }}
            .sc-gauge  {{ width:200px; height:200px; margin:auto 50px; }}
            .sc-background {{ position:relative; height:100px; margin-bottom:10px; background-color:#fff; border-radius:150px 150px 0 0; overflow:hidden; text-align:center; }}
            .sc-mask {{ position:absolute; top:20px; right:20px; left:20px; height:80px; background-color:#555888; border-radius:150px 150px 0 0 }}
            .sc-percentage {{ position:absolute; top:100px; left:-200%; width:400%; height:400%; margin-left:100px; background-color:#00aeef; }}
            .sc-percentage {{ transform:rotate({tacho}deg); transform-origin:top center; }}
            .sc-min {{ float:left; }}
            .sc-max {{ float:right; }}
            .sc-value {{ position:absolute; top:50%; left:0; width:100%;  font-size:48px; font-weight:700 }}
            </style>
            </body>
            </html>
            """
    return html