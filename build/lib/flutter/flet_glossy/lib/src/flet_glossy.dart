import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:glossy/glossy.dart';

class FletGlossyControl extends StatelessWidget {
  final Control? parent;
  final Control control;

  const FletGlossyControl({
    super.key,
    required this.parent,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    String text = control.attrString("value", "")!;
    double width = control.attrDouble("width", 200.0) ?? 200.0;
    double height = control.attrDouble("height", 200.0) ?? 200.0;
    double border_radius = control.attrDouble("border_radius", 12.0) ?? 12.0;
    double fontSize = control.attrDouble("font_size", 20.0) ?? 20.0;

    String? fontWeightStr = control.attrString("font_weight");
    FontWeight fontWeight = switch (fontWeightStr.toLowerCase()) {
      "w100" => FontWeight.w100,
      "w200" => FontWeight.w200,
      "w300" => FontWeight.w300,
      "w400" => FontWeight.w400,
      "w500" => FontWeight.w500,
      "w600" => FontWeight.w600,
      "w700" => FontWeight.w700,
      "w800" => FontWeight.w800,
      "w900" => FontWeight.w900,
      "bold" => FontWeight.bold,
      _ => FontWeight.normal,
    };

    String? colorStr = control.attrString("color");
    Color color = colorStr != null
        ? Color(int.parse(colorStr.replaceFirst("#", "0xff")))
        : Colors.white;

    Widget myControl = Align(
      alignment: Alignment.center,
      child: GlossyContainer(
        width: width,
        height: height,
        borderRadius: BorderRadius.circular(border_radius),
        child: Center(
          child: Text(
            text,
            style: TextStyle(
              fontSize: fontSize,
              fontWeight: fontWeight,
              color: color,
            ),
          ),
        ),
      ),
    );

    return constrainedControl(context, myControl, parent, control);
  }
}
