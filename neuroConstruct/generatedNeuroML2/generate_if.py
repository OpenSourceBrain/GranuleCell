
from pyneuroml.analysis import generate_current_vs_frequency_curve

simulator = 'jNeuroML'

res_1_jnml = generate_current_vs_frequency_curve(nml2_file =          'Granule_98.cell.nml', 
                                                 cell_id =            'Granule_98', 
                                                 start_amp_nA =       0, 
                                                 end_amp_nA =         0.08, 
                                                 step_nA =            0.005, 
                                                 analysis_duration =  1500, 
                                                 analysis_delay =     50,
                                                 dt =                 0.01,
                                                 plot_voltage_traces= False,
                                                 temperature=         "32degC",
                                                 simulator =          simulator,
                                                 plot_if =            False)

simulator = 'jNeuroML_NEURON'

res_1_jnrn = generate_current_vs_frequency_curve(nml2_file =          'Granule_98.cell.nml', 
                                                 cell_id =            'Granule_98', 
                                                 start_amp_nA =       0, 
                                                 end_amp_nA =         0.08, 
                                                 step_nA =            0.005, 
                                                 analysis_duration =  1500, 
                                                 analysis_delay =     50,
                                                 dt =                 0.01,
                                                 plot_voltage_traces= False,
                                                 temperature=         "32degC",
                                                 simulator =          simulator,
                                                 plot_if =            False)
                                                 
                                                 

simulator = 'jNeuroML_NEURON'


from matplotlib import pyplot as plt

plt.xlabel('Input current (nA)')
plt.ylabel('Firing frequency (Hz)')
plt.grid('on')

plt.plot(res_1_jnml.keys(), res_1_jnml.values(), 'o', label="jNeuroML")
plt.plot(res_1_jnrn.keys(), res_1_jnrn.values(), 'o', label="jNeuroML_NEURON")

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=3)

plt.show()
