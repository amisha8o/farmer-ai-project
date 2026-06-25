def predict_crop(temp, rain, soil):

    if soil.lower()=="black" and rain>=170:

        crop="Rice"
        score="95%"
        advice="High food sustainability"

    elif soil.lower()=="red" and temp>=32:

        crop="Maize"
        score="88%"
        advice="Moderate sustainability"

    else:

        crop="Wheat"
        score="82%"
        advice="Suitable crop"

    return crop, score, advice