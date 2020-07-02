package com.YOUR.PACKAGE;

import android.content.res.Resources;

public class ConvertPxDp {
    public ConvertPxDp(){

    }
    public int dpToPx(int dp)
    {
        return (int) (dp * Resources.getSystem().getDisplayMetrics().density);
    }
    public int pxToDp(int px)
    {
        return (int) (px / Resources.getSystem().getDisplayMetrics().density);
    }
}
