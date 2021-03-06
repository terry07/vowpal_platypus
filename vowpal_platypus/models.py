from vw import VW

def vw_model(model_params, node=False):
    params = model_params.copy()
    if node is not False:
        assert params.get('cores'), '`cores` parameter must specify the total number of cores to make a multi-core model.'
        multicore_params = {
            'total': params['cores'],
            'node': node,
            'holdout_off': True,
            'span_server': 'localhost'
        }
        params.update(multicore_params)
        if not params.get('unique_id'):
            params['unique_id'] = 0
    if params.get('cores'):
        params.pop('cores')
    return VW(params)

def model(model_params):
    cores = model_params.get('cores')
    if cores is not None and cores > 1:
        return [vw_model(model_params, node=n) for n in range(cores)]
    else:
        return vw_model(model_params)

def linear_regression(**model_params):
    return model(model_params)

def als(**model_params):
    return model(model_params)

def logistic_regression(**model_params):
    model_params.update({'link': 'logistic', 'loss': 'logistic'})
    return model(model_params)
