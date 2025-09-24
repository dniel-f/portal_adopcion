BEGIN;
--
-- Create model Mascota
--
CREATE TABLE "mascotas_mascota" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(100) NOT NULL, "especie" varchar(50) NOT NULL, "raza" varchar(50) NOT NULL, "edad" integer unsigned NOT NULL CHECK ("edad" >= 0), "sexo" varchar(10) NOT NULL, "tamaño" varchar(20) NOT NULL, "estado_salud" text NOT NULL, "descripcion" text NOT NULL, "fecha_registro" datetime NOT NULL, "disponible" bool NOT NULL, "ubicacion" varchar(100) NOT NULL);
--
-- Create model CustomUser
--
CREATE TABLE "mascotas_customuser" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "telefono" varchar(20) NOT NULL, "direccion" varchar(200) NOT NULL);
CREATE TABLE "mascotas_customuser_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "customuser_id" bigint NOT NULL REFERENCES "mascotas_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "mascotas_customuser_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "customuser_id" bigint NOT NULL REFERENCES "mascotas_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model PublicacionBlog
--
CREATE TABLE "mascotas_publicacionblog" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "titulo" varchar(200) NOT NULL, "contenido" text NOT NULL, "fecha_publicacion" datetime NOT NULL, "autor_id" bigint NOT NULL REFERENCES "mascotas_customuser" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model SolicitudAdopcion
--
CREATE TABLE "mascotas_solicitudadopcion" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "fecha_solicitud" datetime NOT NULL, "estado" varchar(20) NOT NULL, "comentario" text NOT NULL, "mascota_id" bigint NOT NULL REFERENCES "mascotas_mascota" ("id") DEFERRABLE INITIALLY DEFERRED, "usuario_id" bigint NOT NULL REFERENCES "mascotas_customuser" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "mascotas_customuser_groups_customuser_id_group_id_fefccd9f_uniq" ON "mascotas_customuser_groups" ("customuser_id", "group_id");
CREATE INDEX "mascotas_customuser_groups_customuser_id_73ff07c9" ON "mascotas_customuser_groups" ("customuser_id");
CREATE INDEX "mascotas_customuser_groups_group_id_14f98b3e" ON "mascotas_customuser_groups" ("group_id");
CREATE UNIQUE INDEX "mascotas_customuser_user_permissions_customuser_id_permission_id_fba785e1_uniq" ON "mascotas_customuser_user_permissions" ("customuser_id", "permission_id");
CREATE INDEX "mascotas_customuser_user_permissions_customuser_id_e7066bc6" ON "mascotas_customuser_user_permissions" ("customuser_id");
CREATE INDEX "mascotas_customuser_user_permissions_permission_id_70d90c03" ON "mascotas_customuser_user_permissions" ("permission_id");
CREATE INDEX "mascotas_publicacionblog_autor_id_8b135c84" ON "mascotas_publicacionblog" ("autor_id");
CREATE INDEX "mascotas_solicitudadopcion_mascota_id_384c10a3" ON "mascotas_solicitudadopcion" ("mascota_id");
CREATE INDEX "mascotas_solicitudadopcion_usuario_id_48871197" ON "mascotas_solicitudadopcion" ("usuario_id");
COMMIT;
BEGIN;
--
-- Remove field comentario from solicitudadopcion
--
ALTER TABLE "mascotas_solicitudadopcion" DROP COLUMN "comentario";
--
-- Add field mensaje to solicitudadopcion
--
ALTER TABLE "mascotas_solicitudadopcion" ADD COLUMN "mensaje" text NULL;
COMMIT;
BEGIN;
--
-- Create model FotoMascota
--
CREATE TABLE "mascotas_fotomascota" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "imagen" varchar(100) NOT NULL, "descripcion" varchar(200) NOT NULL, "mascota_id" bigint NOT NULL REFERENCES "mascotas_mascota" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "mascotas_fotomascota_mascota_id_a07cd2e5" ON "mascotas_fotomascota" ("mascota_id");
COMMIT;
BEGIN;
--
-- Change Meta options on customuser
--
-- (no-op)
--
-- Change Meta options on fotomascota
--
-- (no-op)
--
-- Change Meta options on mascota
--
-- (no-op)
--
-- Change Meta options on publicacionblog
--
-- (no-op)
--
-- Change Meta options on solicitudadopcion
--
-- (no-op)
--
-- Alter field estado_salud on mascota
--
CREATE TABLE "new__mascotas_mascota" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "estado_salud" varchar(100) NOT NULL, "nombre" varchar(100) NOT NULL, "especie" varchar(50) NOT NULL, "raza" varchar(50) NOT NULL, "edad" integer unsigned NOT NULL CHECK ("edad" >= 0), "sexo" varchar(10) NOT NULL, "tamaño" varchar(20) NOT NULL, "descripcion" text NOT NULL, "fecha_registro" datetime NOT NULL, "disponible" bool NOT NULL, "ubicacion" varchar(100) NOT NULL);
INSERT INTO "new__mascotas_mascota" ("id", "nombre", "especie", "raza", "edad", "sexo", "tamaño", "descripcion", "fecha_registro", "disponible", "ubicacion", "estado_salud") SELECT "id", "nombre", "especie", "raza", "edad", "sexo", "tamaño", "descripcion", "fecha_registro", "disponible", "ubicacion", "estado_salud" FROM "mascotas_mascota";
DROP TABLE "mascotas_mascota";
ALTER TABLE "new__mascotas_mascota" RENAME TO "mascotas_mascota";
--
-- Alter field autor on publicacionblog
--
-- (no-op)
--
-- Alter field mascota on solicitudadopcion
--
-- (no-op)
--
-- Alter field usuario on solicitudadopcion
--
-- (no-op)
COMMIT;
BEGIN;
--
-- Create constraint unique_usuario_mascota on model solicitudadopcion
--
CREATE TABLE "new__mascotas_solicitudadopcion" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "fecha_solicitud" datetime NOT NULL, "estado" varchar(20) NOT NULL, "mascota_id" bigint NOT NULL REFERENCES "mascotas_mascota" ("id") DEFERRABLE INITIALLY DEFERRED, "usuario_id" bigint NOT NULL REFERENCES "mascotas_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "mensaje" text NULL, CONSTRAINT "unique_usuario_mascota" UNIQUE ("usuario_id", "mascota_id"));
INSERT INTO "new__mascotas_solicitudadopcion" ("id", "fecha_solicitud", "estado", "mascota_id", "usuario_id", "mensaje") SELECT "id", "fecha_solicitud", "estado", "mascota_id", "usuario_id", "mensaje" FROM "mascotas_solicitudadopcion";
DROP TABLE "mascotas_solicitudadopcion";
ALTER TABLE "new__mascotas_solicitudadopcion" RENAME TO "mascotas_solicitudadopcion";
CREATE INDEX "mascotas_solicitudadopcion_mascota_id_384c10a3" ON "mascotas_solicitudadopcion" ("mascota_id");
CREATE INDEX "mascotas_solicitudadopcion_usuario_id_48871197" ON "mascotas_solicitudadopcion" ("usuario_id");
COMMIT;
BEGIN;
--
-- Change Meta options on customuser
--
-- (no-op)
--
-- Change Meta options on fotomascota
--
-- (no-op)
--
-- Change Meta options on mascota
--
-- (no-op)
--
-- Change Meta options on publicacionblog
--
-- (no-op)
--
-- Change Meta options on solicitudadopcion
--
-- (no-op)
--
-- Remove constraint unique_usuario_mascota from model solicitudadopcion
--
CREATE TABLE "new__mascotas_solicitudadopcion" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "fecha_solicitud" datetime NOT NULL, "estado" varchar(20) NOT NULL, "mascota_id" bigint NOT NULL REFERENCES "mascotas_mascota" ("id") DEFERRABLE INITIALLY DEFERRED, "usuario_id" bigint NOT NULL REFERENCES "mascotas_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "mensaje" text NULL);
INSERT INTO "new__mascotas_solicitudadopcion" ("id", "fecha_solicitud", "estado", "mascota_id", "usuario_id", "mensaje") SELECT "id", "fecha_solicitud", "estado", "mascota_id", "usuario_id", "mensaje" FROM "mascotas_solicitudadopcion";
DROP TABLE "mascotas_solicitudadopcion";
ALTER TABLE "new__mascotas_solicitudadopcion" RENAME TO "mascotas_solicitudadopcion";
CREATE INDEX "mascotas_solicitudadopcion_mascota_id_384c10a3" ON "mascotas_solicitudadopcion" ("mascota_id");
CREATE INDEX "mascotas_solicitudadopcion_usuario_id_48871197" ON "mascotas_solicitudadopcion" ("usuario_id");
--
-- Alter field estado_salud on mascota
--
CREATE TABLE "new__mascotas_mascota" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(100) NOT NULL, "especie" varchar(50) NOT NULL, "raza" varchar(50) NOT NULL, "edad" integer unsigned NOT NULL CHECK ("edad" >= 0), "sexo" varchar(10) NOT NULL, "tamaño" varchar(20) NOT NULL, "descripcion" text NOT NULL, "fecha_registro" datetime NOT NULL, "disponible" bool NOT NULL, "ubicacion" varchar(100) NOT NULL, "estado_salud" text NOT NULL);
INSERT INTO "new__mascotas_mascota" ("id", "nombre", "especie", "raza", "edad", "sexo", "tamaño", "descripcion", "fecha_registro", "disponible", "ubicacion", "estado_salud") SELECT "id", "nombre", "especie", "raza", "edad", "sexo", "tamaño", "descripcion", "fecha_registro", "disponible", "ubicacion", "estado_salud" FROM "mascotas_mascota";
DROP TABLE "mascotas_mascota";
ALTER TABLE "new__mascotas_mascota" RENAME TO "mascotas_mascota";
--
-- Alter field autor on publicacionblog
--
-- (no-op)
--
-- Alter field mascota on solicitudadopcion
--
-- (no-op)
--
-- Alter field usuario on solicitudadopcion
--
-- (no-op)
COMMIT;
