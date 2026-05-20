from collections import OrderedDict

dnn_input_variables = OrderedDict(
    {
        "higgs1_reco_pt": ["HiggsLeading", "pt"],
        "higgs1_reco_eta": ["HiggsLeading", "eta"],
        "higgs1_reco_mass": ["HiggsLeading", "mass_regr"],
        "higgs1_btagBB_wp": ["HiggsLeading", "btagBB_3wp"],
        "higgs2_reco_pt": ["HiggsSubLeading", "pt"],
        "higgs2_reco_eta": ["HiggsSubLeading", "eta"],
        "higgs2_btagBB_wp": ["HiggsSubLeading", "btagBB_3wp"],
        "hh_vec_mass": ["HH", "mass"],
        "hh_vec_pt": ["HH", "pt"],
        "hh_vec_eta": ["HH", "eta"],
        "higgs1_DeltaR_Hj": ["HiggsLeading", "dR_Hjet_min"],
        "higgs1_mass_Hj": ["HiggsLeading", "m_Hjet_min_dR"],
        "higgs2_DeltaR_Hj": ["HiggsSubLeading", "dR_Hjet_min"],
        "higgs2_mass_Hj": ["HiggsSubLeading", "m_Hjet_min_dR"],
        "met_et": ["MET", "sumEt"],
    }
)
