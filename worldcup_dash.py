import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
import plotly.express as px
import pandas as pd
import numpy as np

# Load and prepare data
df = pd.read_csv('matches_1930_2022.csv')

# Create additional columns for analysis
df['Total Goals'] = df['home_score'] + df['away_score']
df['Decade'] = (df['Year'] // 10) * 10

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

url_tema_claro = dbc.themes.PULSE
url_tema_escuro = dbc.themes.CYBORG

tema_claro = 'pulse'
tema_escuro = 'cyborg'

app.layout = dbc.Container([
    dcc.Tabs(id='main_tab', value='tab1-overview', 
            children=[
                dcc.Tab(label='World Cup Overview', value='tab1-overview'),
                dcc.Tab(label='Team Performance', value='tab2-teams'),
                dcc.Tab(label='Head-to-Head', value='tab3-h2h'),
                dcc.Tab(label='Goals Analysis', value='tab4-goals')
            ]),
    html.Div(id='render_page')
])

@app.callback(Output('render_page', 'children'),
                Input('main_tab', 'value'))
def RenderTab(tab):
    if tab == 'tab1-overview':
        return html.Div([
            dbc.Row([
                dbc.Col([
                    html.H1('FIFA World Cup Dashboard')
                ]),
                dbc.Col([
                    ThemeSwitchAIO(aio_id='tema_switch', 
                                    themes=[url_tema_claro, url_tema_escuro])
                ])
            ]),
            
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        html.H4('Select Year Range:')
                    ]),
                    dbc.Row([
                        dcc.RangeSlider(
                            id='year-slider',
                            min=1930,
                            max=2022,
                            step=4,
                            marks={year: str(year) for year in range(1930, 2023, 8)},
                            value=[1990, 2022]
                        )
                    ])
                ], width=12)
            ]),
            
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='goals-per-year')
                ], width=12)
            ]),
            
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='goals-per-decade')
                ], width=12)
            ])
        ])
    
    elif tab == 'tab2-teams':
        return html.Div([
            dbc.Row([
                dbc.Col([
                    html.H1('Team Performance Analysis')
                ]),
                dbc.Col([
                    ThemeSwitchAIO(aio_id='tema_switch', 
                                    themes=[url_tema_claro, url_tema_escuro])
                ])
            ]),
            
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        html.H4('Select Team:')
                    ]),
                    dbc.Row([
                        dcc.Dropdown(
                            id='team-selector',
                            options=[{'label': team, 'value': team} for team in pd.concat([df['home_team'], df['away_team']]).unique()],
                            value='Brazil',
                            multi=False
                        )
                    ])
                ], width=6),
                
                dbc.Col([
                    dbc.Row([
                        html.H4('Select Year Range:')
                    ]),
                    dbc.Row([
                        dcc.RangeSlider(
                            id='team-year-slider',
                            min=1930,
                            max=2022,
                            step=4,
                            marks={year: str(year) for year in range(1930, 2023, 8)},
                            value=[1930, 2022]
                        )
                    ])
                ], width=6)
            ]),
            
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='team-performance')
                ], width=12)
            ]),
            
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='team-goals-timeline')
                ], width=12)
            ]),
            
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='team-round-performance')
                ], width=12)
            ])
        ])
    
    elif tab == 'tab3-h2h':
        return html.Div([
            dbc.Row([
                dbc.Col([
                    html.H1('Head-to-Head Comparison')
                ]),
                dbc.Col([
                    ThemeSwitchAIO(aio_id='tema_switch', 
                                    themes=[url_tema_claro, url_tema_escuro])
                ])
            ]),
            
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        html.H4('Select Team 1:')
                    ]),
                    dbc.Row([
                        dcc.Dropdown(
                            id='team1-selector',
                            options=[{'label': team, 'value': team} for team in pd.concat([df['home_team'], df['away_team']]).unique()],
                            value='Brazil',
                            multi=False
                        )
                    ])
                ], width=6),
                
                dbc.Col([
                    dbc.Row([
                        html.H4('Select Team 2:')
                    ]),
                    dbc.Row([
                        dcc.Dropdown(
                            id='team2-selector',
                            options=[{'label': team, 'value': team} for team in pd.concat([df['home_team'], df['away_team']]).unique()],
                            value='Argentina',
                            multi=False
                        )
                    ])
                ], width=6)
            ]),
            
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        html.H4('Select Year Range:')
                    ]),
                    dbc.Row([
                        dcc.RangeSlider(
                            id='h2h-year-slider',
                            min=1930,
                            max=2022,
                            step=4,
                            marks={year: str(year) for year in range(1930, 2023, 8)},
                            value=[1930, 2022]
                        )
                    ])
                ], width=12)
            ]),
            
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='h2h-results')
                ], width=6),
                
                dbc.Col([
                    dcc.Graph(id='h2h-goals')
                ], width=6)
            ]),
            
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='h2h-matches')
                ], width=12)
            ])
        ])
    
    elif tab == 'tab4-goals':
        return html.Div([
            dbc.Row([
                dbc.Col([
                    html.H1('Goals Analysis')
                ]),
                dbc.Col([
                    ThemeSwitchAIO(aio_id='tema_switch', 
                                    themes=[url_tema_claro, url_tema_escuro])
                ])
            ]),
            
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        html.H4('Select Teams:')
                    ]),
                    dbc.Row([
                        dcc.Dropdown(
                            id='goals-team-selector',
                            options=[{'label': team, 'value': team} for team in pd.concat([df['home_team'], df['away_team']]).unique()],
                            value=['Brazil', 'Argentina', 'Germany', 'France'],
                            multi=True
                        )
                    ])
                ], width=6),
                
                dbc.Col([
                    dbc.Row([
                        html.H4('Select Year Range:')
                    ]),
                    dbc.Row([
                        dcc.RangeSlider(
                            id='goals-year-slider',
                            min=1930,
                            max=2022,
                            step=4,
                            marks={year: str(year) for year in range(1930, 2023, 8)},
                            value=[1930, 2022]
                        )
                    ])
                ], width=6)
            ]),
            
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='team-goals-per-year')
                ], width=12)
            ]),
            
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='avg-goals-per-worldcup')
                ], width=12)
            ])
        ])

# Callbacks for Overview tab
@app.callback(
    [Output('goals-per-year', 'figure'),
     Output('goals-per-decade', 'figure')],
    [Input('year-slider', 'value'),
     Input(ThemeSwitchAIO.ids.switch('tema_switch'), 'value')]
)
def update_overview_charts(year_range, tema_switch):
    tema = tema_claro if tema_switch else tema_escuro
    filtered_df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
    
    # Goals per year
    goals_per_year = filtered_df.groupby('Year')['Total Goals'].sum().reset_index()
    fig1 = px.line(goals_per_year, x='Year', y='Total Goals', 
                   title='Total Goals per World Cup',
                   template=tema)
    
    # Goals per decade
    goals_per_decade = filtered_df.groupby('Decade')['Total Goals'].sum().reset_index()
    fig2 = px.bar(goals_per_decade, x='Decade', y='Total Goals', 
                  title='Total Goals per Decade',
                  template=tema)
    
    return fig1, fig2

# Callbacks for Team Performance tab
@app.callback(
    [Output('team-performance', 'figure'),
     Output('team-goals-timeline', 'figure'),
     Output('team-round-performance', 'figure')],
    [Input('team-selector', 'value'),
     Input('team-year-slider', 'value'),
     Input(ThemeSwitchAIO.ids.switch('tema_switch'), 'value')]
)
def update_team_charts(team, year_range, tema_switch):
    tema = tema_claro if tema_switch else tema_escuro
    filtered_df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
    
    # Get all matches for the selected team
    team_matches = filtered_df[(filtered_df['home_team'] == team) | (filtered_df['away_team'] == team)].copy()
    
    # Calculate results
    team_matches['Result'] = team_matches.apply(
        lambda x: 'Win' if (
            (x['home_team'] == team and x['home_score'] > x['away_score']) or
            (x['away_team'] == team and x['away_score'] > x['home_score'])
        ) else ('Draw' if x['home_score'] == x['away_score'] else 'Loss'),
        axis=1
    )
    
    # Team performance by year
    performance_by_year = team_matches.groupby(['Year', 'Result']).size().unstack().fillna(0).reset_index()
    fig1 = px.bar(performance_by_year, x='Year', y=['Win', 'Draw', 'Loss'], 
                  title=f'{team} Performance by World Cup',
                  labels={'value': 'Number of Matches', 'variable': 'Result'},
                  template=tema)
    
    # Team goals timeline
    team_matches['Goals For'] = team_matches.apply(
        lambda x: x['home_score'] if x['home_team'] == team else x['away_score'], axis=1)
    team_matches['Goals Against'] = team_matches.apply(
        lambda x: x['away_score'] if x['home_team'] == team else x['home_score'], axis=1)
    
    goals_timeline = team_matches.groupby('Year')[['Goals For', 'Goals Against']].sum().reset_index()
    fig2 = px.line(goals_timeline, x='Year', y=['Goals For', 'Goals Against'], 
                   title=f'{team} Goals Timeline',
                   labels={'value': 'Goals', 'variable': 'Type'},
                   template=tema)
    
    # Performance by round
    round_performance = team_matches.groupby(['Round', 'Result']).size().unstack().fillna(0).reset_index()
    fig3 = px.bar(round_performance, x='Round', y=['Win', 'Draw', 'Loss'],
                  title=f'{team} Performance by Round',
                  labels={'value': 'Number of Matches', 'variable': 'Result'},
                  template=tema)
    
    return fig1, fig2, fig3

# Callbacks for Head-to-Head tab
@app.callback(
    [Output('h2h-results', 'figure'),
     Output('h2h-goals', 'figure'),
     Output('h2h-matches', 'figure')],
    [Input('team1-selector', 'value'),
     Input('team2-selector', 'value'),
     Input('h2h-year-slider', 'value'),
     Input(ThemeSwitchAIO.ids.switch('tema_switch'), 'value')]
)
def update_h2h_charts(team1, team2, year_range, tema_switch):
    tema = tema_claro if tema_switch else tema_escuro
    filtered_df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
    
    # Get matches between the two teams
    h2h_matches = filtered_df[((filtered_df['home_team'] == team1) & (filtered_df['away_team'] == team2)) | 
                              ((filtered_df['home_team'] == team2) & (filtered_df['away_team'] == team1))].copy()
    
    # Calculate results from team1's perspective
    h2h_matches['Result'] = h2h_matches.apply(
        lambda x: 'Win' if (
            (x['home_team'] == team1 and x['home_score'] > x['away_score']) or
            (x['away_team'] == team1 and x['away_score'] > x['home_score'])
        ) else ('Draw' if x['home_score'] == x['away_score'] else 'Loss'),
        axis=1
    )
    
    # Results pie chart
    results = h2h_matches['Result'].value_counts().reset_index()
    results.columns = ['Result', 'Count']
    fig1 = px.pie(results, values='Count', names='Result', 
                  title=f'{team1} vs {team2} Results ({year_range[0]}-{year_range[1]})',
                  template=tema)
    
    # Goals comparison
    team1_goals = h2h_matches.apply(
        lambda x: x['home_score'] if x['home_team'] == team1 else x['away_score'], axis=1).sum()
    team2_goals = h2h_matches.apply(
        lambda x: x['away_score'] if x['home_team'] == team1 else x['home_score'], axis=1).sum()
    
    goals_df = pd.DataFrame({
        'Team': [team1, team2],
        'Goals': [team1_goals, team2_goals]
    })
    
    fig2 = px.bar(goals_df, x='Team', y='Goals', 
                  title=f'Total Goals in Head-to-Head Matches',
                  template=tema)
    
    # Matches timeline
    if not h2h_matches.empty:
        h2h_matches['Match'] = h2h_matches['home_team'] + ' vs ' + h2h_matches['away_team']
        h2h_matches['Score'] = h2h_matches['home_score'].astype(str) + '-' + h2h_matches['away_score'].astype(str)
        fig3 = px.scatter(h2h_matches, x='Year', y='Match', color='Result',
                          hover_data=['Score', 'Round', 'Venue'],
                          title=f'Head-to-Head Matches Timeline',
                          template=tema)
    else:
        fig3 = px.scatter(title='No matches found between these teams in selected period',
                         template=tema)
    
    return fig1, fig2, fig3

# Callbacks for Goals Analysis tab
@app.callback(
    [Output('team-goals-per-year', 'figure'),
     Output('avg-goals-per-worldcup', 'figure')],
    [Input('goals-team-selector', 'value'),
     Input('goals-year-slider', 'value'),
     Input(ThemeSwitchAIO.ids.switch('tema_switch'), 'value')]
)
def update_goals_charts(teams, year_range, tema_switch):
    tema = tema_claro if tema_switch else tema_escuro
    filtered_df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
    
    # Prepare data for goals per year per team
    goals_data = []
    for team in teams:
        team_matches = filtered_df[(filtered_df['home_team'] == team) | (filtered_df['away_team'] == team)].copy()
        team_matches['Goals'] = team_matches.apply(
            lambda x: x['home_score'] if x['home_team'] == team else x['away_score'], axis=1)
        
        goals_by_year = team_matches.groupby('Year')['Goals'].sum().reset_index()
        goals_by_year['Team'] = team
        goals_data.append(goals_by_year)
    
    if goals_data:
        goals_df = pd.concat(goals_data)
        fig1 = px.line(goals_df, x='Year', y='Goals', color='Team',
                      title='Goals per World Cup by Team',
                      template=tema)
    else:
        fig1 = px.line(title='No data available for selected teams/period',
                      template=tema)
    
    # Average goals per World Cup
    avg_goals = filtered_df.groupby('Year')['Total Goals'].mean().reset_index()
    fig2 = px.bar(avg_goals, x='Year', y='Total Goals',
                 title='Average Goals per Match by World Cup',
                 template=tema)
    
    return fig1, fig2

if __name__ == '__main__':
    app.run(port=8051)