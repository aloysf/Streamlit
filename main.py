import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math

st.title("Taylor expansion")
a = st.slider("$\\omega$", 0.0, 20.0, 1.0, 0.1)
N_ord = st.slider("$N$", 0, 20, 1, 1)

st.latex(r'''
    \sin(x)=\sum_{i=0}^N (-1)^i\frac{x^{2i+1}}{(2i+1)!}=x-\frac{x^3}{6}+\ldots
    ''')

fig, ax = plt.subplots()

x_plot = np.linspace(-2,2,500)
y = lambda x: np.sin(a*x)
ax.plot(x_plot, y(x_plot), label = "sin(x)")

approx = np.zeros(len(x_plot))
for i in range(N_ord):
    approx += (-1)**i *(a*x_plot)**(2*i+1) / float(math.factorial(2*i+1))

ax.plot(x_plot, approx, label = "Taylor approximation")
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)

ax.legend(loc=1)

st.pyplot(fig)