def find_subfamily(ori_family):
    family = None
    subfamily = None
    if "biggan" in ori_family:
        family = "biggan"
        subfamily = ori_family
        # add_item_into_list("biggan", family, families1)
    elif "compare_gan" in ori_family:
        family = "compare_gan"
        subfamily = ori_family
        # add_item_into_list("compare_gan", family, families1)
    elif "image_augmentation" in ori_family:
        family = "image_augmentation"
        subfamily = ori_family
        # add_item_into_list("image_augmentation", family, families1)
    elif "imagenet-inception" in ori_family or ori_family == "tf2-preview-inception_v3":
        family = "imagenet-inception"
        subfamily = ori_family
        # add_item_into_list("imagenet-inception", family, families1)
    elif "imagenet-mobilenet" in ori_family or ori_family == "quantops" or ori_family == "tf2-preview-mobilenet_v2":
        family = "imagenet-mobilenet"
        subfamily = ori_family
        # add_item_into_list("imagenet-mobilenet", family, families1)
    elif "imagenet-resnet" in ori_family:
        family = "imagenet-resnet"
        subfamily = ori_family
        # add_item_into_list("imagenet-resnet", family, families1)
    elif "nnlm" in ori_family:
        family = "nnlm"
        subfamily = ori_family
        # add_item_into_list("nnlm", family, families1)
    elif "universal-sentence-encoder" in ori_family:
        family = "universal-sentence-encoder"
        subfamily = ori_family
        # add_item_into_list("universal-sentence-encoder", family, families1)
    else:
        family = ori_family
        subfamily = None
        # families1.append(family)
    return family, subfamily