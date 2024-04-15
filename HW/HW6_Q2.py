def find_store_or_product(id, store_rev, product_scales_cnt):
    if ord(id[0]) <= 57 and ord(id[0]) >= 48:
        if product_scales_cnt.get(int(id)) is not None:
            result = product_scales_cnt[int(id)]
        else:
            raise KeyError
    else:
        if store_rev.get(id) is not None:
            result = store_rev[id]
        else:
            raise KeyError

    return result
