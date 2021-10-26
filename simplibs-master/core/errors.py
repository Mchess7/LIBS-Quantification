import numpy as np



def mean_absolute_error(targets, predictions):
    
    MAE = 0
        
    for i in range(0,len(targets)):
        MAE += np.abs(targets[i]-predictions[i])
        
    return MAE/len(targets)



def mean_square_error(targets, predictions):
    
    MSE = 0
        
    for i in range(0,len(targets)):
        MSE += np.abs(targets[i]-predictions[i])**2
        
    return MSE/len(targets)


def root_mean_square_error(targets, predictions):
        
    return np.sqrt(mean_square_error(targets, predictions))



def mean_absolute_percentage_error(targets, predictions):
    
    MAPE = 0
        
    for i in range(0,len(targets)):
        MAPE += np.abs((targets[i]-predictions[i])/targets[i])
        
    return 100*MAPE/len(targets)


def max_error(targets, predictions):
    
    ME = []
        
    for i in range(0,len(targets)):
        ME.append(np.abs(targets[i]-predictions[i]))
        
    return max(ME)


def max_squared_error(targets, predictions):
    
    MSE = []
        
    for i in range(0,len(targets)):
        MSE.append(np.abs(targets[i]-predictions[i])**2)
        
    return max(MSE)



def max_percentage_error(targets, predictions):
    
    MPE = []
        
    for i in range(0,len(targets)):
        MPE.append(np.abs((targets[i]-predictions[i])/targets[i]))
        
    return 100 * max(MPE)



def r_squared(targets, predictions):
    
    mean = 0
    
    for i in range(0,len(targets)):
        mean += targets[i]
    
    mean = np.mean(targets)
    
    sqerror = 0
    sqdiff = 0
    
    for j in range(0,len(targets)):
        sqerror += (targets[i]-predictions[i])**2
        sqdiff += (targets[i]-mean)**2
        
    R2 = sqerror/sqdiff
    
    return 1 - R2
