import plotly.figure_factory as ff

df = [dict(Task="Levantamentos dos requisitos", Start='2020-02-01', Finish='2020-03-01'),
      dict(Task="Escolha dos componentes", Start='2020-02-01', Finish='2020-03-07'),
      dict(Task="Att. do documento", Start='2020-03-15', Finish='2020-04-07'),
      dict(Task="Projeto dos circuitos", Start='2020-03-01', Finish='2020-04-15'),
      dict(Task="Desenho da PCB", Start='2020-04-15', Finish='2020-06-01'),
      dict(Task="Finalização do documento", Start='2020-06-01', Finish='2020-06-20')]


fig = ff.create_gantt(df)
fig.update_layout(
    title="TCC2 Planejamento",
    xaxis_title="Datas",
    yaxis_title="Tarefas"
)
fig.show()

# import plotly.figure_factory as ff

# df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
#       dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
#       dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]

# fig = ff.create_gantt(df)
# fig.show()