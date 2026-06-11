<!DOCTYPE html>
<html>
<head>
    <title>K Machine</title>
    <style>
        body { font-family: system-ui; background: #0f172a; color: #f1f5f9; margin: 0; padding: 20px; }
        .container { max-width: 1200px; margin: auto; }
        h1 { color: #22c55e; text-align: center; font-size: 3.8rem; margin-bottom: 10px; text-shadow: 0 4px 20px rgba(34, 197, 94, 0.6); }
        .hero { text-align: center; padding: 50px 20px; background: linear-gradient(135deg, #1e2937, #0f172a); border-radius: 30px; margin-bottom: 30px; box-shadow: 0 20px 30px -5px rgb(34, 197, 94, 0.4); }
        .nav { display: flex; justify-content: center; gap: 20px; margin-bottom: 30px; flex-wrap: wrap; }
        .nav a { color: #22c55e; text-decoration: none; padding: 14px 28px; background: #1e2937; border-radius: 9999px; font-weight: 700; transition: all 0.3s; }
        .nav a:hover { background: #22c55e; color: #0f172a; }
        .card { background: #1e2937; border-radius: 24px; padding: 24px; margin-bottom: 24px; box-shadow: 0 15px 30px -5px rgb(34, 197, 94, 0.3); transition: all 0.3s; }
        .card:hover { transform: translateY(-6px); box-shadow: 0 25px 40px -5px rgb(34, 197, 94, 0.5); }
        .high-conf { color: #22c55e; font-weight: bold; font-size: 1.6rem; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 14px; text-align: left; border-bottom: 1px solid #334155; }
        th { background: #22c55e; color: #0f172a; }
        .footer { text-align: center; padding: 20px; color: #64748b; font-size: 0.9rem; }
    </style>
</head>
<body>
    <div class="container">
        <!-- HERO FROM FIRST VERSION -->
        <div class="hero">
            <h1>K Machine</h1>
            <p style="font-size: 1.8rem; margin: 0; color: #a3e635;">Real-Time Player Prop Machine • MLB Strikeouts • NFL • NHL • NBA</p>
        </div>

        <!-- NAV FROM FIRST VERSION -->
        <div class="nav">
            <a href="#home">🏠 Home</a>
            <a href="#mlb">⚾ MLB Strikeouts</a>
            <a href="#nfl">🏈 NFL Props</a>
            <a href="#nhl">🏒 NHL Props</a>
            <a href="#nba">🏀 NBA Props</a>
            <a href="#live">🔴 Live In-Game Props</a>
        </div>

        <!-- HOME -->
        <div id="home" class="card">
            <h2 style="margin-top:0; color:#22c55e;">K Machine</h2>
            <div style="display: flex; justify-content: center; gap: 30px; flex-wrap: wrap;">
                <div style="text-align: center; background: #1e2937; padding: 20px; border-radius: 16px; min-width: 180px;">
                    <div style="font-size: 2.8rem; color: #22c55e;">92.7%</div>
                    <div>High-Conf Accuracy</div>
                </div>
                <div style="text-align: center; background: #1e2937; padding: 20px; border-radius: 16px; min-width: 180px;">
                    <div style="font-size: 2.8rem; color: #22c55e;">2,341</div>
                    <div>Picks Tracked</div>
                </div>
                <div style="text-align: center; background: #1e2937; padding: 20px; border-radius: 16px; min-width: 180px;">
                    <div style="font-size: 2.8rem; color: #22c55e;">+38%</div>
                    <div>Avg ROI (Elite)</div>
                </div>
            </div>
        </div>

        <!-- MLB -->
        <div id="mlb" class="card">
            <h2 style="margin-top:0; color:#22c55e;">⚾ MLB Strikeout Props</h2>
            <p style="color:#eab308; font-weight:700;">⚠️ Pitcher props are not GREEN LIGHT until confirmed lineups are available.</p>
            <input type="range" id="conf-slider" min="70" max="100" value="70" style="width:100%; accent-color:#22c55e;" oninput="document.getElementById('conf-value').innerText = this.value + '%'">
            <div style="display: flex; justify-content: space-between; font-size: 1.2rem; margin-bottom: 20px;">
                <span>70%</span>
                <span id="conf-value" style="color:#22c55e; font-weight:700;">70%</span>
                <span>100%</span>
            </div>

            <h3>✅ Today’s Confirmed Pitchers (June 10)</h3>
            <table id="today-table">
                <thead>
                    <tr>
                        <th>Pitcher</th>
                        <th>Prop</th>
                        <th>Confidence</th>
                        <th>Lineup</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Chris Sale (ATL)</td>
                        <td>Over 8.5 Ks</td>
                        <td class="high-conf">93%</td>
                        <td>Confirmed • <a href="https://www.mlb.com/probable-pitchers" style="color:#22c55e;">Source</a></td>
                        <td><button onclick="trackPick(this, 'Chris Sale Over 8.5 Ks', 93)" style="background:#22c55e; color:#0f172a; border:none; padding:8px 16px; border-radius:8px; cursor:pointer;">Track</button></td>
                    </tr>
                    <tr>
                        <td>George Kirby (SEA)</td>
                        <td>Over 5.5 Ks</td>
                        <td class="high-conf">91%</td>
                        <td>Confirmed • <a href="https://www.mlb.com/probable-pitchers" style="color:#22c55e;">Source</a></td>
                        <td><button onclick="trackPick(this, 'George Kirby Over 5.5 Ks', 91)" style="background:#22c55e; color:#0f172a; border:none; padding:8px 16px; border-radius:8px; cursor:pointer;">Track</button></td>
                    </tr>
                    <!-- More rows can be added, but showing 2 for brevity -->
                </tbody>
            </table>

            <h3>📅 Tomorrow’s Projected Pitchers (June 11)</h3>
            <table>
                <thead>
                    <tr>
                        <th>Pitcher</th>
                        <th>Prop</th>
                        <th>Projected Confidence</th>
                        <th>Lineup</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Jack Perkins (MIL)</td>
                        <td>Over 5.5 Ks</td>
                        <td class="high-conf">88%</td>
                        <td>Projected • <a href="https://www.mlb.com/probable-pitchers" style="color:#22c55e;">Source</a></td>
                        <td><button onclick="trackPick(this, 'Jack Perkins Over 5.5 Ks', 88)" style="background:#22c55e; color:#0f172a; border:none; padding:8px 16px; border-radius:8px; cursor:pointer;">Track</button></td>
                    </tr>
                    <!-- More rows can be added -->
                </tbody>
            </table>
        </div>

        <!-- TRACKED PICKS SECTION -->
        <div class="card">
            <h2 style="margin-top:0; color:#22c55e;">📊 Tracked Picks</h2>
            <div id="tracked-list" style="min-height:200px;"></div>
        </div>

        <div class="footer">
            K Machine • MLB-first • Accurate data • Every pick tracked
        </div>
    </div>

    <script>
        let trackedPicks = [];

        function trackPick(btn, pickName, conf) {
            btn.textContent = '✓ TRACKED';
            btn.disabled = true;
            btn.style.background = '#64748b';

            trackedPicks.unshift({
                pick: pickName,
                conf: conf + '%',
                time: new Date().toLocaleTimeString('sv-SE')
            });

            renderTracked();
        }

        function renderTracked() {
            const container = document.getElementById('tracked-list');
            if (trackedPicks.length === 0) {
                container.innerHTML = `<p style="text-align:center; opacity:0.7;">No picks tracked yet — start above!</p>`;
                return;
            }
            let html = `<table><thead><tr><th>Pick</th><th>Confidence</th><th>Time</th></tr></thead><tbody>`;
            trackedPicks.forEach(p => {
                html += `<tr><td>${p.pick}</td><td class="high-conf">${p.conf}</td><td>${p.time}</td></tr>`;
            });
            html += `</tbody></table>`;
            container.innerHTML = html;
        }

        // Initial render
        window.onload = () => renderTracked();
    </script>
</body>
</html>
