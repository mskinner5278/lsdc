=================================
LSDC Gui Installation
=================================
2022-07-08
=================================
Steps
-----

1. make sym-links for startup scripts
..
::
    cd /usr/local/bin
    dzdo ln -s /nsls2/software/mx/daq/lsdc_nyx/bin/lsdcGui_nyx lsdcGui

2. install custom gui conda environment
..
::
    explorer.nsls2.bnl.gov/job_templates
    "Conda - Install custom code env (lsdc-gui)"

3. make sym-links for conda environment current version to latest
..
:: 
    dzdo ln -s /opt/conda/envs/conda/lsdc-gui-x.x.x /opt/conda/envs/conda/lsdc-gui-latest
4. install albula
..
::
    dectris.com download 
