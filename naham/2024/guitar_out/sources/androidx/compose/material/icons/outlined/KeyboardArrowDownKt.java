package androidx.compose.material.icons.outlined;

import androidx.compose.material.icons.Icons;
import androidx.compose.ui.graphics.Color;
import androidx.compose.ui.graphics.SolidColor;
import androidx.compose.ui.graphics.StrokeCap;
import androidx.compose.ui.graphics.StrokeJoin;
import androidx.compose.ui.graphics.vector.ImageVector;
import androidx.compose.ui.graphics.vector.PathBuilder;
import androidx.compose.ui.graphics.vector.VectorKt;
import androidx.compose.ui.unit.Dp;
import kotlin.Metadata;
import kotlin.jvm.internal.Intrinsics;

/* compiled from: KeyboardArrowDown.kt */
@Metadata(d1 = {"\u0000\u0010\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\"\u0010\u0010\u0000\u001a\u0004\u0018\u00010\u0001X\u0082\u000e¢\u0006\u0002\n\u0000\"\u0015\u0010\u0002\u001a\u00020\u0001*\u00020\u00038F¢\u0006\u0006\u001a\u0004\b\u0004\u0010\u0005¨\u0006\u0006"}, d2 = {"_keyboardArrowDown", "Landroidx/compose/ui/graphics/vector/ImageVector;", "KeyboardArrowDown", "Landroidx/compose/material/icons/Icons$Outlined;", "getKeyboardArrowDown", "(Landroidx/compose/material/icons/Icons$Outlined;)Landroidx/compose/ui/graphics/vector/ImageVector;", "material-icons-core_release"}, k = 2, mv = {1, 8, 0}, xi = 48)
/* loaded from: classes.dex */
public final class KeyboardArrowDownKt {
    private static ImageVector _keyboardArrowDown;

    public static final ImageVector getKeyboardArrowDown(Icons.Outlined outlined) {
        ImageVector.Builder m3254addPathoIyEayM;
        Intrinsics.checkNotNullParameter(outlined, "<this>");
        ImageVector imageVector = _keyboardArrowDown;
        if (imageVector != null) {
            Intrinsics.checkNotNull(imageVector);
            return imageVector;
        }
        ImageVector.Builder builder = new ImageVector.Builder("Outlined.KeyboardArrowDown", Dp.m4873constructorimpl(24.0f), Dp.m4873constructorimpl(24.0f), 24.0f, 24.0f, 0L, 0, false, 224, null);
        int defaultFillType = VectorKt.getDefaultFillType();
        SolidColor solidColor = new SolidColor(Color.INSTANCE.m2655getBlack0d7_KjU(), null);
        int m2975getButtKaPHkGw = StrokeCap.INSTANCE.m2975getButtKaPHkGw();
        int m2985getBevelLxFBmk8 = StrokeJoin.INSTANCE.m2985getBevelLxFBmk8();
        PathBuilder pathBuilder = new PathBuilder();
        pathBuilder.moveTo(7.41f, 8.59f);
        pathBuilder.lineTo(12.0f, 13.17f);
        pathBuilder.lineToRelative(4.59f, -4.58f);
        pathBuilder.lineTo(18.0f, 10.0f);
        pathBuilder.lineToRelative(-6.0f, 6.0f);
        pathBuilder.lineToRelative(-6.0f, -6.0f);
        pathBuilder.lineToRelative(1.41f, -1.41f);
        pathBuilder.close();
        m3254addPathoIyEayM = builder.m3254addPathoIyEayM(pathBuilder.getNodes(), (r30 & 2) != 0 ? VectorKt.getDefaultFillType() : defaultFillType, (r30 & 4) != 0 ? "" : "", (r30 & 8) != 0 ? null : solidColor, (r30 & 16) != 0 ? 1.0f : 1.0f, (r30 & 32) == 0 ? null : null, (r30 & 64) != 0 ? 1.0f : 1.0f, (r30 & 128) != 0 ? 0.0f : 1.0f, (r30 & 256) != 0 ? VectorKt.getDefaultStrokeLineCap() : m2975getButtKaPHkGw, (r30 & 512) != 0 ? VectorKt.getDefaultStrokeLineJoin() : m2985getBevelLxFBmk8, (r30 & 1024) != 0 ? 4.0f : 1.0f, (r30 & 2048) != 0 ? 0.0f : 0.0f, (r30 & 4096) == 0 ? 0.0f : 1.0f, (r30 & 8192) == 0 ? 0.0f : 0.0f);
        ImageVector build = m3254addPathoIyEayM.build();
        _keyboardArrowDown = build;
        Intrinsics.checkNotNull(build);
        return build;
    }
}