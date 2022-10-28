# Functions to plot and save the fano fitting results
# Jiaming He (UT Austin) 10/28/2022

import matplotlib.pyplot as plt # For doing the plots
from matplotlib import gridspec
import pandas as pd
from Fano_peaks import afano, twofano, threefano, fourfano

def onepeakfig(pressure ,sample, peak_number, fit_shift, fit_int, residual_fano, popt_fano, perr_fano, asymm_factor, asymm_factor_err):
    fig = plt.figure(figsize=(5,10))
    gs = gridspec.GridSpec(3,1, height_ratios=[1,0.3,0.2])
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])
    ax3 = fig.add_subplot(gs[2])
    ax1.plot(fit_shift,fit_int,'ro',markersize=6)
    ax1.plot(fit_shift, afano(fit_shift, *popt_fano), 'k--')#,\
    ax2.plot(fit_shift, residual_fano, "bo")
    ax2.set_xlabel("Raman Shift cm$^{-1}$",family="sans",  fontsize=12)
    ax1.set_ylabel("Normalized Intensity",family="sans",  fontsize=12)
    ax2.set_ylabel("Residual",family="sans",  fontsize=12)
    ax3.axis('off')
    ax3.text(-0.2,0.2,'Sample '+ str(sample)+ ' '+str(pressure) + ' Peak '+str(peak_number)+' fitting report:', fontsize = 12, fontweight="bold")
    ax3.text(-0.2,0, "Fano. Omega = %0.6f (+/-) %0.6f" % (popt_fano[0], perr_fano[0]), fontsize = 12)
    ax3.text(-0.2,-0.2, "Fano. Gamma = %0.6f (+/-) %0.6f" % (popt_fano[1], perr_fano[1]), fontsize = 12)
    ax3.text(-0.2,-0.4, "Fano. Asymm. param = %0.6f (+/-) %0.6f" % (popt_fano[2], perr_fano[2]), fontsize = 12)
    ax3.text(-0.2,-0.6, "Fano. Asymm. factor = %0.6f (+/-) %0.6f" % (asymm_factor, asymm_factor_err), fontsize = 12)
    ax3.text(-0.2,-0.8, "Fano. int0 = %0.6f (+/-) %0.6f" % (popt_fano[3], perr_fano[3]), fontsize = 12)
    ax3.text(-0.2,-1, "Fano. bg. const. = %0.6f (+/-) %0.6f" % (popt_fano[4], perr_fano[4]), fontsize = 12)
    ax3.text(-0.2,-1.2, "Fano. bg. slope. = %0.6f (+/-) %0.6f" % (popt_fano[5], perr_fano[5]), fontsize = 12)
    return fig

def twopeakfig(pressure ,sample, peak_number, fit_shift, fit_int, residual_fano, popt_fano, perr_fano, asymm_factor, asymm_factor_err):
    fig = plt.figure(figsize=(8,12))
    gs = gridspec.GridSpec(4,1, height_ratios=[1,0.3,0.2,0.2])
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])
    ax3 = fig.add_subplot(gs[2])
    ax4 = fig.add_subplot(gs[3])
    # create a new plot for showing the spectrum
    ax1.plot(fit_shift,fit_int,'ro',markersize=6)
    #ax1.plot(fit_shift, _1gaussian(fit_shift, *popt_gauss), 'k--')#,\
    ax1.plot(fit_shift, twofano(fit_shift, *popt_fano), 'k--')#,\
    #ax1.plot(fit_shift, voigt_peak_1, "g")
    ax2.plot(fit_shift, residual_fano, "bo")
    ax2.set_xlabel("Raman Shift cm$^{-1}$",family="sans",  fontsize=12)
    ax1.set_ylabel("Normalized Intensity",family="sans",  fontsize=12)
    ax2.set_ylabel("Residual",family="sans",  fontsize=12)
    ax3.axis('off')
    ax3.text(-0.2,0.2,'Sample '+ str(sample)+ ' '+str(pressure) + ' Peak '+str(peak_number)+' fitting report:', fontsize = 12, fontweight="bold")
    ax3.text(-0.2,0, "Peak 1 Fano. Omega = %0.6f (+/-) %0.6f" % (popt_fano[0], perr_fano[0]), fontsize = 12)
    ax3.text(-0.2,-0.2, "Peak 1 Fano. Gamma = %0.6f (+/-) %0.6f" % (popt_fano[1], perr_fano[1]), fontsize = 12)
    ax3.text(-0.2,-0.4, "Peak 1 Fano. Asymm. param = %0.6f (+/-) %0.6f" % (popt_fano[2], perr_fano[2]), fontsize = 12)
    ax3.text(-0.2,-0.6, "Peak 1 Fano. Asymm. factor = %0.6f (+/-) %0.6f" % (asymm_factor, asymm_factor_err), fontsize = 12)
    ax3.text(-0.2,-0.8, "Peak 1 Fano. int0 = %0.6f (+/-) %0.6f" % (popt_fano[3], perr_fano[3]), fontsize = 12)
    ax3.text(-0.2,-1, "Peak 1 Fano. bg. const. = %0.6f (+/-) %0.6f" % (popt_fano[4], perr_fano[4]), fontsize = 12)
    ax3.text(-0.2,-1.2, "Peak 1 Fano. bg. slope. = %0.6f (+/-) %0.6f" % (popt_fano[5], perr_fano[5]), fontsize = 12)
    ax4.axis('off')
    ax4.text(-0.2,0, "Peak 2 Fano. Omega = %0.6f (+/-) %0.6f" % (popt_fano[6], perr_fano[6]), fontsize = 12)
    ax4.text(-0.2,-0.2, "Peak 2 Fano. Gamma = %0.6f (+/-) %0.6f" % (popt_fano[7], perr_fano[7]), fontsize = 12)
    ax4.text(-0.2,-0.4, "Peak 2 Fano. Asymm. param = %0.6f (+/-) %0.6f" % (popt_fano[8], perr_fano[8]), fontsize = 12)
    ax4.text(-0.2,-0.6, "Peak 2 Fano. Asymm. factor = %0.6f (+/-) %0.6f" % (asymm_factor, asymm_factor_err), fontsize = 12)
    ax4.text(-0.2,-0.8, "Peak 2 Fano. int0 = %0.6f (+/-) %0.6f" % (popt_fano[9], perr_fano[9]), fontsize = 12)
    ax4.text(-0.2,-1, "Peak 2 Fano. bg. const. = %0.6f (+/-) %0.6f" % (popt_fano[10], perr_fano[10]), fontsize = 12)
    ax4.text(-0.2,-1.2, "Peak 2 Fano. bg. slope. = %0.6f (+/-) %0.6f" % (popt_fano[11], perr_fano[11]), fontsize = 12)
    return fig

def threepeakfig(pressure ,sample, peak_number, fit_shift, fit_int, residual_fano, popt_fano, perr_fano, asymm_factor, asymm_factor_err):
    fig = plt.figure(figsize=(8,12))
    gs = gridspec.GridSpec(4,1, height_ratios=[1,0.3,0.2,0.2])
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])
    ax3 = fig.add_subplot(gs[2])
    ax4 = fig.add_subplot(gs[3])
    # create a new plot for showing the spectrum
    ax1.plot(fit_shift,fit_int,'ro',markersize=6)
    #ax1.plot(fit_shift, _1gaussian(fit_shift, *popt_gauss), 'k--')#,\
    ax1.plot(fit_shift, threefano(fit_shift, *popt_fano), 'k--')#,\
    #ax1.plot(fit_shift, voigt_peak_1, "g")
    ax2.plot(fit_shift, residual_fano, "bo")
    ax2.set_xlabel("Raman Shift cm$^{-1}$",family="sans",  fontsize=12)
    ax1.set_ylabel("Normalized Intensity",family="sans",  fontsize=12)
    ax2.set_ylabel("Residual",family="sans",  fontsize=12)
    ax3.axis('off')
    ax3.text(-0.2,0.2,'Sample '+ str(sample)+ ' '+str(pressure) + ' Peak '+str(peak_number)+' fitting report:', fontsize = 12, fontweight="bold")
    ax3.text(-0.2,0, "Peak 1 Fano. Omega = %0.6f (+/-) %0.6f" % (popt_fano[0], perr_fano[0]), fontsize = 12)
    ax3.text(-0.2,-0.2, "Peak 1 Fano. Gamma = %0.6f (+/-) %0.6f" % (popt_fano[1], perr_fano[1]), fontsize = 12)
    ax3.text(-0.2,-0.4, "Peak 1 Fano. Asymm. param = %0.6f (+/-) %0.6f" % (popt_fano[2], perr_fano[2]), fontsize = 12)
    ax3.text(-0.2,-0.6, "Peak 1 Fano. Asymm. factor = %0.6f (+/-) %0.6f" % (asymm_factor, asymm_factor_err), fontsize = 12)
    ax3.text(-0.2,-0.8, "Peak 1 Fano. int0 = %0.6f (+/-) %0.6f" % (popt_fano[3], perr_fano[3]), fontsize = 12)
    ax3.text(-0.2,-1, "Peak 1 Fano. bg. const. = %0.6f (+/-) %0.6f" % (popt_fano[4], perr_fano[4]), fontsize = 12)
    ax3.text(-0.2,-1.2, "Peak 1 Fano. bg. slope. = %0.6f (+/-) %0.6f" % (popt_fano[5], perr_fano[5]), fontsize = 12)
    ax4.axis('off')
    ax4.text(-0.2,0, "Peak 2 Fano. Omega = %0.6f (+/-) %0.6f" % (popt_fano[6], perr_fano[6]), fontsize = 12)
    ax4.text(-0.2,-0.2, "Peak 2 Fano. Gamma = %0.6f (+/-) %0.6f" % (popt_fano[7], perr_fano[7]), fontsize = 12)
    ax4.text(-0.2,-0.4, "Peak 2 Fano. Asymm. param = %0.6f (+/-) %0.6f" % (popt_fano[8], perr_fano[8]), fontsize = 12)
    #ax4.text(-0.2,-0.6, "Peak 2 Fano. Asymm. factor = %0.6f (+/-) %0.6f" % (asymm_factor, asymm_factor_err), fontsize = 12)
    ax4.text(-0.2,-0.8, "Peak 2 Fano. int0 = %0.6f (+/-) %0.6f" % (popt_fano[9], perr_fano[9]), fontsize = 12)
    ax4.text(-0.2,-1, "Peak 2 Fano. bg. const. = %0.6f (+/-) %0.6f" % (popt_fano[10], perr_fano[10]), fontsize = 12)
    ax4.text(-0.2,-1.2, "Peak 2 Fano. bg. slope. = %0.6f (+/-) %0.6f" % (popt_fano[11], perr_fano[11]), fontsize = 12)
    ax4.text(-0.2,-1.4, "Peak 4.3 Fano. Omega = %0.6f (+/-) %0.6f" % (popt_fano[12], perr_fano[12]), fontsize = 12)
    ax4.text(-0.2,-1.6, "Peak 4.3 Fano. Gamma = %0.6f (+/-) %0.6f" % (popt_fano[13], perr_fano[13]), fontsize = 12)
    ax4.text(-0.2,-1.8, "Peak 4.3 Fano. Asymm. param = %0.6f (+/-) %0.6f" % (popt_fano[14], perr_fano[14]), fontsize = 12)
    #ax4.text(-0.2,-2.0, "Peak 4.3 Fano. Asymm. factor = %0.6f (+/-) %0.6f" % (asymm_factor, asymm_factor_err), fontsize = 12)
    ax4.text(-0.2,-2.2, "Peak 4.3 Fano. int0 = %0.6f (+/-) %0.6f" % (popt_fano[15], perr_fano[15]), fontsize = 12)
    ax4.text(-0.2,-2.4, "Peak 4.3 Fano. bg. const. = %0.6f (+/-) %0.6f" % (popt_fano[16], perr_fano[16]), fontsize = 12)
    ax4.text(-0.2,-2.6, "Peak 4.3 Fano. bg. slope. = %0.6f (+/-) %0.6f" % (popt_fano[17], perr_fano[17]), fontsize = 12)
    return fig

def fourpeakfig(pressure ,sample, peak_number, fit_shift, fit_int, residual_fano, popt_fano, perr_fano, asymm_factor, asymm_factor_err):
    fig = plt.figure(figsize=(8,12))
    gs = gridspec.GridSpec(4,1, height_ratios=[1,0.3,0.2,0.2])
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])
    ax3 = fig.add_subplot(gs[2])
    ax4 = fig.add_subplot(gs[3])
    # create a new plot for showing the spectrum
    ax1.plot(fit_shift,fit_int,'ro',markersize=6)
    #ax1.plot(fit_shift, _1gaussian(fit_shift, *popt_gauss), 'k--')#,\
    ax1.plot(fit_shift, fourfano(fit_shift, *popt_fano), 'k--')#,\
    #ax1.plot(fit_shift, voigt_peak_1, "g")
    ax2.plot(fit_shift, residual_fano, "bo")
    ax2.set_xlabel("Raman Shift cm$^{-1}$",family="sans",  fontsize=12)
    ax1.set_ylabel("Normalized Intensity",family="sans",  fontsize=12)
    ax2.set_ylabel("Residual",family="sans",  fontsize=12)
    ax3.axis('off')
    ax3.text(-0.2,0.2,'Sample '+ str(sample)+ ' '+str(pressure) + ' Peak '+str(peak_number)+' fitting report:', fontsize = 12, fontweight="bold")
    ax3.text(-0.2,0, "Peak 1 Fano. Omega = %0.6f (+/-) %0.6f" % (popt_fano[0], perr_fano[0]), fontsize = 12)
    ax3.text(-0.2,-0.2, "Peak 1 Fano. Gamma = %0.6f (+/-) %0.6f" % (popt_fano[1], perr_fano[1]), fontsize = 12)
    ax3.text(-0.2,-0.4, "Peak 1 Fano. Asymm. param = %0.6f (+/-) %0.6f" % (popt_fano[2], perr_fano[2]), fontsize = 12)
    ax3.text(-0.2,-0.6, "Peak 1 Fano. Asymm. factor = %0.6f (+/-) %0.6f" % (asymm_factor, asymm_factor_err), fontsize = 12)
    ax3.text(-0.2,-0.8, "Peak 1 Fano. int0 = %0.6f (+/-) %0.6f" % (popt_fano[3], perr_fano[3]), fontsize = 12)
    ax3.text(-0.2,-1, "Peak 1 Fano. bg. const. = %0.6f (+/-) %0.6f" % (popt_fano[4], perr_fano[4]), fontsize = 12)
    ax3.text(-0.2,-1.2, "Peak 1 Fano. bg. slope. = %0.6f (+/-) %0.6f" % (popt_fano[5], perr_fano[5]), fontsize = 12)
    ax4.axis('off')
    ax4.text(-0.2,0, "Peak 2 Fano. Omega = %0.6f (+/-) %0.6f" % (popt_fano[6], perr_fano[6]), fontsize = 12)
    ax4.text(-0.2,-0.2, "Peak 2 Fano. Gamma = %0.6f (+/-) %0.6f" % (popt_fano[7], perr_fano[7]), fontsize = 12)
    ax4.text(-0.2,-0.4, "Peak 2 Fano. Asymm. param = %0.6f (+/-) %0.6f" % (popt_fano[8], perr_fano[8]), fontsize = 12)
    #ax4.text(-0.2,-0.6, "Peak 2 Fano. Asymm. factor = %0.6f (+/-) %0.6f" % (asymm_factor, asymm_factor_err), fontsize = 12)
    ax4.text(-0.2,-0.8, "Peak 2 Fano. int0 = %0.6f (+/-) %0.6f" % (popt_fano[9], perr_fano[9]), fontsize = 12)
    ax4.text(-0.2,-1, "Peak 2 Fano. bg. const. = %0.6f (+/-) %0.6f" % (popt_fano[10], perr_fano[10]), fontsize = 12)
    ax4.text(-0.2,-1.2, "Peak 2 Fano. bg. slope. = %0.6f (+/-) %0.6f" % (popt_fano[11], perr_fano[11]), fontsize = 12)
    ax4.text(-0.2,-1.4, "Peak 4.3 Fano. Omega = %0.6f (+/-) %0.6f" % (popt_fano[12], perr_fano[12]), fontsize = 12)
    ax4.text(-0.2,-1.6, "Peak 4.3 Fano. Gamma = %0.6f (+/-) %0.6f" % (popt_fano[13], perr_fano[13]), fontsize = 12)
    ax4.text(-0.2,-1.8, "Peak 4.3 Fano. Asymm. param = %0.6f (+/-) %0.6f" % (popt_fano[14], perr_fano[14]), fontsize = 12)
    #ax4.text(-0.2,-2.0, "Peak 4.3 Fano. Asymm. factor = %0.6f (+/-) %0.6f" % (asymm_factor, asymm_factor_err), fontsize = 12)
    ax4.text(-0.2,-2.2, "Peak 4.3 Fano. int0 = %0.6f (+/-) %0.6f" % (popt_fano[15], perr_fano[15]), fontsize = 12)
    ax4.text(-0.2,-2.4, "Peak 4.3 Fano. bg. const. = %0.6f (+/-) %0.6f" % (popt_fano[16], perr_fano[16]), fontsize = 12)
    ax4.text(-0.2,-2.6, "Peak 4.3 Fano. bg. slope. = %0.6f (+/-) %0.6f" % (popt_fano[17], perr_fano[17]), fontsize = 12)

    ax4.text(-0.2,-2.8, "Peak 4.4 Fano. Omega = %0.6f (+/-) %0.6f" % (popt_fano[18], perr_fano[18]), fontsize = 12)
    ax4.text(-0.2,-3, "Peak 4.4 Fano. Gamma = %0.6f (+/-) %0.6f" % (popt_fano[19], perr_fano[19]), fontsize = 12)
    ax4.text(-0.2,-3.2, "Peak 4.4 Fano. Asymm. param = %0.6f (+/-) %0.6f" % (popt_fano[20], perr_fano[20]), fontsize = 12)
    #ax4.text(-0.2,-3.4, "Peak 4.4 Fano. Asymm. factor = %0.6f (+/-) %0.6f" % (asymm_factor, asymm_factor_err), fontsize = 12)
    ax4.text(-0.2,-3.6, "Peak 4.4 Fano. int0 = %0.6f (+/-) %0.6f" % (popt_fano[21], perr_fano[21]), fontsize = 12)
    ax4.text(-0.2,-3.8, "Peak 4.4 Fano. bg. const. = %0.6f (+/-) %0.6f" % (popt_fano[22], perr_fano[22]), fontsize = 12)
    ax4.text(-0.2,-4, "Peak 4.4 Fano. bg. slope. = %0.6f (+/-) %0.6f" % (popt_fano[23], perr_fano[23]), fontsize = 12)
    return fig

def saveparams (pressure ,sample, peak_number, popt_fano, perr_fano):
    fitting_params = pd.DataFrame(popt_fano, index = ['P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Omega','P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Gamma' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Asymm. Param' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_int', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_bg. const','P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_bg. slope'])
    fitting_err = pd.DataFrame(perr_fano, index = ['P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Omega_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Gamma_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Asymm. Param_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_int_err', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_bg. const_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_bg. slope_err'])
    #asymm = pd.DataFrame(asymm_factor, index = ['P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_asym_factor'])
    
    #asymm_err = pd.DataFrame(asymm_factor_err, index = ['P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_asym_factor_err'])
    frames = [fitting_params, fitting_err]
    result = pd.concat(frames)
    return(result)

def twopeaks_saveparams (pressure ,sample, peak_number, popt_fano, perr_fano):
    fitting_params = pd.DataFrame(popt_fano, index = ['P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Omega','P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Gamma' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Asymm. Param' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_int', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_bg. const','P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_bg. slope', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_Omega','P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_Gamma' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_Asymm. Param' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_int', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_bg. const','P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_bg. slope'])
    fitting_err = pd.DataFrame(perr_fano, index = ['P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Omega_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Gamma_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Asymm. Param_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_int_err', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_bg. const_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_bg. slope_err', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_Omega_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_Gamma_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_Asymm. Param_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_int_err', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_bg. const_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_bg. slope_err'])
    #asymm = pd.DataFrame(asymm_factor, index = ['P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_asym_factor'])
    
    #asymm_err = pd.DataFrame(asymm_factor_err, index = ['P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_asym_factor_err'])
    frames = [fitting_params, fitting_err]
    result = pd.concat(frames)
    return(result)

def threepeaks_saveparams (pressure ,sample, peak_number, popt_fano, perr_fano):
    fitting_params = pd.DataFrame(popt_fano, index = ['P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Omega','P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Gamma' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Asymm. Param' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_int', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_bg. const','P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_bg. slope', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_Omega','P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_Gamma' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_Asymm. Param' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_int', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_bg. const','P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_bg. slope','P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_Omega','P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_Gamma' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_Asymm. Param' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_int', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_bg. const','P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_bg. slope'])
    fitting_err = pd.DataFrame(perr_fano, index = ['P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Omega_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Gamma_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Asymm. Param_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_int_err', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_bg. const_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_bg. slope_err', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_Omega_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_Gamma_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_Asymm. Param_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_int_err', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_bg. const_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_bg. slope_err', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_Omega_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_Gamma_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_Asymm. Param_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_int_err', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_bg. const_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_bg. slope_err'])
    #asymm = pd.DataFrame(asymm_factor, index = ['P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_asym_factor'])
    
    #asymm_err = pd.DataFrame(asymm_factor_err, index = ['P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_asym_factor_err'])
    frames = [fitting_params, fitting_err]
    result = pd.concat(frames)
    return(result)

def fourpeaks_saveparams (pressure ,sample, peak_number, popt_fano, perr_fano):
    fitting_params = pd.DataFrame(popt_fano, index = ['P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Omega','P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Gamma' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Asymm. Param' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_int', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_bg. const','P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_bg. slope', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_Omega','P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_Gamma' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_Asymm. Param' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_int', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_bg. const','P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_bg. slope','P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_Omega','P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_Gamma' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_Asymm. Param' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_int', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_bg. const','P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_bg. slope', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_d'+ str(peak_number)+'_Omega','P'+str(pressure[0])+ '_'+str(sample) + '_peak_d'+ str(peak_number)+'_Gamma' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_d'+ str(peak_number)+'_Asymm. Param' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_d'+ str(peak_number)+'_int', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_d'+ str(peak_number)+'_bg. const','P'+str(pressure[0])+ '_'+str(sample) + '_peak_d'+ str(peak_number)+'_bg. slope'])
    fitting_err = pd.DataFrame(perr_fano, index = ['P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Omega_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Gamma_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_Asymm. Param_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_int_err', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_bg. const_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_bg. slope_err', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_Omega_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_Gamma_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_Asymm. Param_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_int_err', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_bg. const_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_b'+ str(peak_number)+'_bg. slope_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_Omega_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_Gamma_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_Asymm. Param_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_int_err', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_bg. const_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_c'+ str(peak_number)+'_bg. slope_err', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_d'+ str(peak_number)+'_Omega_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_d'+ str(peak_number)+'_Gamma_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_d'+ str(peak_number)+'_Asymm. Param_err' ,'P'+str(pressure[0])+ '_'+str(sample) + '_peak_d'+ str(peak_number)+'_int_err', 'P'+str(pressure[0])+ '_'+str(sample) + '_peak_d'+ str(peak_number)+'_bg. const_err','P'+str(pressure[0])+ '_'+str(sample) + '_peak_d'+ str(peak_number)+'_bg. slope_err'])
    #asymm = pd.DataFrame(asymm_factor, index = ['P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_asym_factor'])
    
    #asymm_err = pd.DataFrame(asymm_factor_err, index = ['P'+str(pressure[0])+ '_'+str(sample) + '_peak_'+ str(peak_number)+'_asym_factor_err'])
    frames = [fitting_params, fitting_err]
    result = pd.concat(frames)
    return(result)