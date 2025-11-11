package com.example.catalogactivity;

import android.content.Intent;
import android.content.res.Configuration;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button btnNavegarDetalle = findViewById(R.id.btn_navegar_detalle);
        btnNavegarDetalle.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Lanzar DetailActivity
                Intent intent = new Intent(MainActivity.this, DetailActivity.class);
                startActivity(intent);


            }
        });

    }
}